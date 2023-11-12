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
        
        self.setGeometry(150, 250, 250, 300)
        self.setWindowTitle('Launch Katana')
        
        self.populateUI()
        self.show()
        
    def populateUI(self):

        layout = QGridLayout()
        arnoldLayout = QVBoxLayout()
        prmanLayout = QGridLayout()

        '''
        tabs that allow you to set your versions of Arnold and Renderman
        as well as the version of Katana that's going to be used with them
        '''

        self.tabs = QTabWidget()
    
         
        '''
        creating and setting up the arnold tab
        '''
        self.arnoldTab = QWidget()
        
        self.checkArnoldVersion = QPushButton('Check for KtoA Versions', self.tabs)
        self.checkArnoldVersion.setCheckable(True)
        self.checkArnoldVersion.clicked.connect(self.displayArnoldTypes)
        
        self.specifyArnoldVersion = QComboBox(self.tabs)

        self.arnoldKatanaVer = self.katanaVersionLabel()
        
        self.selectKatanaVerArnold = self.katanaVersionDropdown()

        arnoldLayout.addWidget(self.checkArnoldVersion)
        arnoldLayout.addWidget(self.specifyArnoldVersion)
        arnoldLayout.addWidget(self.arnoldKatanaVer)
        arnoldLayout.addWidget(self.selectKatanaVerArnold)

        self.arnoldTab.setLayout(arnoldLayout)

    
        '''
        creating and setting up the prman tab
        '''
        self.prmanTab = QWidget()
        self.selectPrmanVer = QLabel('Select PRman Version')
        self.selectProserverVer = QLabel('Select Proserver Version')
        self.prmanVerDropdown = QComboBox()
        
        checkPrman = os.listdir('C:\Program Files\Pixar')
        prefixPrman = 'RenderManForKatana'
        prefixProsever = 'RenderManProServer'

        self.prmanVersionsList = []
        self.proserverList = []

        for version in checkPrman:
            if version.startswith(prefixPrman):
                self.prmanVersionsList.append(version)
            else:
                if version.startswith(prefixProsever):
                    self.proserverList.append(version)
        
        
        self.prmanVerDropdown.addItems(self.prmanVersionsList)
        self.proserverDropdown = QComboBox()
        self.proserverDropdown.addItems(self.proserverList)

        self.prmanKatanaVer = self.katanaVersionLabel()
        
        self.selectKatanaVerPrman = self.katanaVersionDropdown()


        prmanLayout.addWidget(self.selectPrmanVer, 0,0)
        prmanLayout.addWidget(self.selectProserverVer, 0,1)
        prmanLayout.addWidget(self.prmanVerDropdown, 1,0)
        prmanLayout.addWidget(self.proserverDropdown, 1,1)
        prmanLayout.addWidget(self.prmanKatanaVer, 2, 0, 1 , 2)
        prmanLayout.addWidget(self.selectKatanaVerPrman, 3, 0, 1, 2)

        self.prmanTab.setLayout(prmanLayout)

        
        '''
        adding the arnold and renderman tabs to the overall tab box
        '''
        self.tabs.addTab(self.arnoldTab, 'Arnold')
        self.tabs.addTab(self.prmanTab, 'Renderman')


        '''
        Creating the button that's clicked to check to see what version of 
        Katana are currently installed on the user's machine

        '''
        self.checkInstalls = QPushButton('Check for Katana Installs', self)
        self.checkInstalls.setCheckable(True)
        self.checkInstalls.clicked.connect(self.checkInstallsClicked)

        '''
        dropdown that lists all the individual versions of Katana that are installed
        in a specific file driectory.
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
        
        
        '''
        adding all of the above to the QGrid layout. The numbers after the widget
        indicate the row/column that each widget will be placed in.
        '''
        layout.addWidget(self.tabs, 0, 0, 1, 3)
        layout.addWidget(self.checkInstalls, 1, 0, 1, 3)
        layout.addWidget(self.installsDropdown, 2, 0, 1, 3)
        layout.addWidget(self.useRenderman, 3,0)
        layout.addWidget(self.useArnold, 3,1)
        layout.addWidget(self.useDelight, 3,2)
        layout.addWidget(self.launchKatana, 4, 0, 1, 3)

        '''
        packing all of the UI elements into the main window and then laying them 
        out on the window.
        '''
        self.show()
        self.setLayout(layout)
    
    def katanaVersionLabel(self):
        versionLabel = QLabel('What Version of Katana are You Using?')
        return versionLabel

    
    def katanaVersionDropdown(self):
        
        katanaVersions = ['katana2.5',
                          'katana2.6',
                          'katana3.0',
                          'katana3.1',
                          'katana3.2',
                          'katana3.5',
                          'katana3.6',
                          'katana4.0',
                          'katana4.5',
                          'katana5.0',
                          'katana6.0',
                          'katana6.5',
                          'katana7.0']
        
        createComboBox = QComboBox()
        createComboBox.addItems(katanaVersions)
        
        return createComboBox

    
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

    def displayArnoldTypes(self):
        checkArnold = os.listdir('C:\\Users\\AdelePeleschka\\ktoa')

        if self.checkArnoldVersion.isCheckable():
            self.specifyArnoldVersion.addItems(checkArnold)

    
    def proserverVersions(self):
        checkDirectory = os.listdir('C:\Program Files\Pixar')
        prefix = 'RenderManProServer'

        self.proserverVersionsList = []

        for v in checkDirectory:
            if v.startswith(prefix):
                self.proserverVersionsList.append(v)
            else:
                continue

    def loadRenderman(self, checked):
        if checked:
            self.useArnold.setChecked(False)
            self.useArnold.setEnabled(False)
        else:
            self.useArnold.setEnabled(True)
    
    def loadArnold(self, checked):
        if checked:
            self.useRenderman.setChecked(False)
            self.useRenderman.setEnabled(False)
        else:
            self.useRenderman.setEnabled(True)

        
    def launchSelection(self):
        
        launchKatana = os.path.join('C:\\Program Files\\Foundry', self.installsDropdown.currentText(), 'bin\\katanaBin.exe')
        myEnvironment = os.environ.copy()

        #creates path and katana_resources if neither exists in the system's environment variables
        if "KATANA_RESOURCES" not in myEnvironment:
            myEnvironment["KATANA_RESOURCES"] = ""

        if "PATH" not in myEnvironment:
            myEnvironment["PATH"]
        
        myEnvironment["KATANA_ROOT"] = os.path.join('C:\\Program File\\Foundry', self.installsDropdown.currentText())

    
        if self.useDelight.isChecked():
        
            myEnvironment["DEFAULT_RENDERER"] = 'dl'
            myEnvironment["DELIGHT"] = os.path.join('C:\\Program Files\\Foundry', self.installsDropdown.currentText(), '3Delight')
        
            # += takes everything that's already in a variable and adds it to the end of the variable
            myEnvironment["PATH"] += f'{myEnvironment["DELIGHT"]}\\bin'
            myEnvironment["KATANA_RESOURCES"] += f';{myEnvironment["DELIGHT"]}/3DelightForKatana'
            print('load DL')
        
        if self.useArnold.isChecked():
            myEnvironment["DEFAULT_RENDERER"] = 'arnold'
            myEnvironment["KTOA_HOME"] = os.path.join('C:\\Users\\AdelePeleschka\\ktoa', self.specifyArnoldVersion.currentText())

            myEnvironment["PATH"] += f';{myEnvironment["KTOA_HOME"]}\\bin'
            myEnvironment["KATANA_RESOURCES"] += f';{myEnvironment["KTOA_HOME"]}'
            print('Arnold loaded')
        
        if self.useRenderman.isChecked():
            
            myEnvironment["DEFAULT_RENDERER"] = 'prman'
            
            # points to renderman proserver
            myEnvironment["RMANTREE"] = os.path.join('C:\\Program Files\\Pixar', self.proserverDropdown.currentText())
            
            # points to the actual plugin. plugin path is pointing to the version of prman and katana
            # selected in the dropdowns in the launcher window.
            myEnvironment["RFKTREE"] = os.path.join('C:\\Program Files\\Pixar', self.prmanVerDropdown.currentText(), 'plugins', self.selectKatanaVerPrman.currentText())
            
            myEnvironment["KATANA_RESOURCES"] += f';{myEnvironment["RFKTREE"]}'
            
            # workaround to fix ImportError with KatanaQueue
            myEnvironment["PATH"] += f';{myEnvironment["KATANA_ROOT"]}\\bin'

        print(str(myEnvironment["RFKTREE"]))
        print(str(myEnvironment["RMANTREE"]))



    
        subprocess.Popen(launchKatana, env=myEnvironment)


        


app = QApplication(sys.argv)

myWindow = katanaLauncher()
sys.exit(app.exec_())
