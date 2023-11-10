import sys
import os
from os.path import isfile, join
import subprocess
from PyQt5.QtWidgets import *

from PyQt5.QtCore import *

from PyQt5.QtGui import (QFont,
                         QFontDatabase)


class katanaLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.createWindow()
    
    def createWindow(self):
        
        self.setGeometry(250, 250, 350, 300)
        self.setWindowTitle('Launch Katana')
        
        self.populateUI()
        self.show()
        
    def populateUI(self):

        layout = QGridLayout()

        '''
        Creating the button that's clicked to check to see what version of 
        Katana are currently installed on the user's machine

        '''
        self.checkInstalls = QPushButton('Check for Katana Installs', self)
        self.checkInstalls.setCheckable(True)
        self.checkInstalls.clicked.connect(self.checkInstallsClicked)

        '''
        checkboxes where you can specify what renderer to launch Katana
        with. 
        '''
        
        self.useRenderman = QCheckBox('Launch with Renderman', self)
        self.useRenderman.setGeometry(170, 140, 81, 20)
        self.useRenderman.stateChanged.connect(self.loadRenderman)

        self.useArnold = QCheckBox('Launch with Arnold', self)
        self.useArnold.setGeometry(170, 140, 81, 20)
        self.useArnold.stateChanged.connect(self.loadArnold)

        self.useDelight = QCheckBox('Launch with 3Delight', self)
        self.useDelight.setGeometry(170, 140, 81, 20)
        self.useDelight.stateChanged.connect(self.loadDl)
        
        '''
        making the combox that will list all of the currently installed versions
        of Katana when the above button is pressed.

        '''
        self.installsDropdown = QComboBox()
        
        
        '''
        creating the button that launches the version of Katana that was selected
        from the list in the combo box.

        '''        
        self.launchKatana = QPushButton('Launch Katana', self)
        self.launchKatana.setCheckable(True)
        self.launchKatana.clicked.connect(self.launchSelection)

        
        '''
        adding all of the above to the QGrid layout. The numbers after the widget
        indicate the row/column that each widget will be placed in.
        '''
        layout.addWidget(self.checkInstalls, 0, 1)
        layout.addWidget(self.installsDropdown, 1, 1, 2, 3)
        layout.addWidget(self.useRenderman, 2,1)
        layout.addWidget(self.useArnold, 2,2)
        layout.addWidget(self.useDelight, 2,3)
        layout.addWidget(self.launchKatana, 3, 3)

        '''
        packing all of the UI elements into the main window and then laying them 
        out on the window.
        '''
        self.show()
        self.setLayout(layout)
    
    def checkInstallsClicked(self):
        '''
        realised that there are nuke/modo/mari installs in my directory because 
        fninstall puts everything in there. This makes sure that ONLY the katana
        installs are being picked up and added to the combo box/dropdown menu.
        '''
        
        checkDirectory = os.listdir('C:\Program Files\Foundry')
        prefix = 'Katana'

        self.katanaInstalls = []

        for k in checkDirectory:
            if k.startswith(prefix):
                self.katanaInstalls.append(k)
            else:
                continue
  
        '''
        takes the result of the above loop and adds them to the combobox
        '''
        if self.checkInstalls.isCheckable():
            self.installsDropdown.addItems(self.katanaInstalls)


    def loadRenderman(self, checked):
        if checked:
            print('Loaded!')
        else:
            print('not loaded!')
    
    def loadArnold(self, checked):
        if checked:
            print('Loaded!')
        else:
            print('not loaded!')
    
    def loadDl(self, checked):
        if checked:
            print('pls hook me up')
        else:
            print('not done yet :sad:')
            

        
    def launchSelection(self):
        
        launchKatana = os.path.join('C:\\Program Files\\Foundry', self.installsDropdown.currentText(), 'bin\\katanaBin.exe')
        
        # creates a copy of system environment variables
        myEnvironment = os.environ.copy()

        #creates path and katana_resources if neither exists in the system's environment variables
        if "KATANA_RESOURCES" not in myEnvironment:
            myEnvironment["KATANA_RESOURCES"] = ""
        if "PATH" not in myEnvironment:
            myEnvironment["PATH"]
    
        # same setup as writing a launcher script to load in render plugins
        myEnvironment["KATANA_ROOT"] = os.path.join('C:\\Program File\\Foundry', self.installsDropdown.currentText())
        myEnvironment["DEFAULT_RENDERER"] = 'dl'
        myEnvironment["DELIGHT"] = os.path.join('C:\\Program Files\\Foundry', self.installsDropdown.currentText(), '3Delight')
        
        # += takes everything that's already in a variable and adds it to the end of the variable
        myEnvironment["PATH"] += f'{myEnvironment["DELIGHT"]}/bin'
        myEnvironment["KATANA_RESOURCES"] += f';{myEnvironment["DELIGHT"]}/3DelightForKatana'


        
        if self.launchKatana.isCheckable():
            subprocess.Popen(launchKatana, env=myEnvironment)


        


app = QApplication(sys.argv)

myWindow = katanaLauncher()
sys.exit(app.exec_())
