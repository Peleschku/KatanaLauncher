import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QSizePolicy

class buttonWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.createUI() # calls the UI function (see below)

    def createUI(self):

        self.setGeometry(100, 100, 200, 150) #sets the size of the window
        self.setWindowTitle("Adele's Widget") #sets the name of the window
        self.displayButton() #calls the display button function

        self.show() #similar to .pack() in tkinter i think?

    def displayButton(self):
        '''
        nameLable is creating a QLable, which is a container used to add text to a window. .setText() adds the text
        to the container (think .setValue() in katana when changing a parameter.). .move() then allows you to position
        the label on the UI.
        '''
        nameLable = QLabel(self)
        nameLable.setText("click for a surprise") #sets the text above the window
        nameLable.move(60, 30) #positions the button on the UI window

        '''
        below:
        _button_ is creating the button with the QPushButton function that's packaged with PyQt
        _self_ being passed is similar to setting a root node in katana - it parents the button the UI window created by the super()

        adding self before a variable means that the variable can be access from any function within the class.
        '''
        self.button = QPushButton("push me!", self)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.buttonClicked) # when button is clicked, call the buttonClicked function
        self.button.move(60, 60)
        
        self.numberCount = QLabel(self)
        self.currentNumber = 0
        self.numberCount.setNum(self.currentNumber)
        self.numberCount.move(95, 100)
        self.numberCount.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum) # trying to get two numbers to show when the list hits 10 +

    def buttonClicked(self):
        
        self.currentNumber += 1 # takes the currentNumber variable, adds one and then stores the new value in the variable

        if self.button.isCheckable():
            self.numberCount.setNum(self.currentNumber)
  

app = QApplication(sys.argv)

myWindow = buttonWindow()
sys.exit(app.exec_())
