import sys
from os import listdir
from os.path import isfile, join
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QLabel,
                             QPushButton,
                             QVBoxLayout,
                             QComboBox,
                             QGridLayout
                             )

from PyQt5.QtCore import(Qt,
                         QDir
                         )

from PyQt5.QtGui import (QFont,
                         QFontDatabase)

katanaInstalls = listdir('C:\Program Files\Foundry')

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
        layout.addWidget(self.checkInstalls, 0, 2)
        layout.addWidget(self.installsDropdown, 1, 2)
        layout.addWidget(self.launchKatana, 1, 3)

        '''
        packing all of the UI elements into the main window and then laying them 
        out on the window.
        '''
        self.show()
        self.setLayout(layout)
    
    def checkInstallsClicked(self):
        if self.checkInstalls.isCheckable():
            self.installsDropdown.addItems(katanaInstalls) # when the check for installs button is pressed, populate the combo box

    def launchSelection(self):
        if self.launchKatana.isCheckable():
            print(self.installsDropdown.currentText()) # .currrentText grabs the selected text in the dropdown


        


app = QApplication(sys.argv)

myWindow = katanaLauncher()
sys.exit(app.exec_())
