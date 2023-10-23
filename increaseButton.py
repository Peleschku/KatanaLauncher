import sys
import os
from pathlib import Path

from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QLabel,
                             QPushButton,
                             QVBoxLayout,
                             )

from PyQt5.QtCore import(Qt,
                         QDir
                         )

from PyQt5.QtGui import (QFont,
                         QFontDatabase)


class buttonWindow(QWidget):
    def __init__(self):
        super().__init__() # allows you at access parent class 
        self.createUI() # calls the UI function (see below)

    def createUI(self):

        self.setGeometry(250, 250, 350, 300) #sets the size of the window
        self.setWindowTitle("Adele's Widget") #sets the name of the window
        self.displayButton() #calls the display button function

        self.show() #similar to .pack() in tkinter i think?

    def displayButton(self):
        
        '''
        creating a layout for the buttons so I don't need to manually scale/move everything

        '''

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter) # aligns everything globally


        '''
        nameLable is creating a QLable, which is a container used to add text to a window. .setText() adds the text
        to the container (think .setValue() in katana when changing a parameter.). .move() then allows you to position
        the label on the UI.
        '''
        self.nameLable = QLabel(self)
        self.nameLable.setText("Press the button") #sets the text above the window
        self.nameLable.move(60, 30) #positions the button on the UI window
        self.nameLable.setStyleSheet("font: 18pt Courier New")

        '''
        below:
        _button_ is creating the button with the QPushButton function that's packaged with PyQt
        _self_ being passed is similar to setting a root node in katana - it parents the button the UI window created by the super()

        adding self before a variable means that the variable can be access from any function within the class.
        '''
        self.button = QPushButton("Click here!", self)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.buttonClicked) # when button is clicked, call the buttonClicked function
        self.button.setStyleSheet("font: 12pt Courier New")
        
        
        self.numberCount = QLabel(self)
        self.currentNumber = 0
        self.numberCount.setNum(self.currentNumber)
        self.numberCount.setStyleSheet("font: 12pt Courier New")

        layout.addWidget(self.nameLable)
        layout.addWidget(self.button)
        layout.addWidget(self.numberCount)
        layout.setAlignment(self.numberCount, Qt.AlignCenter) # aligns the counter to the center of the widget
        layout.setSpacing(25)

        self.setLayout(layout)

    def buttonClicked(self):
        
        self.currentNumber += 1 # takes the currentNumber variable, adds one and then stores the new value in the variable

        if self.button.isCheckable():
            self.numberCount.setNum(self.currentNumber)
            self.numberCount.adjustSize() # fixes the size of the Qlable so double digits aren't cut off

  

app = QApplication(sys.argv)

myWindow = buttonWindow()
sys.exit(app.exec_())
