import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

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
        nameLable.setText("clikc this button") #sets the text above the window
        nameLable.move(60, 30) #positions the button on the UI window

        '''
        below:
        'button' is creating the button with the QPushButton function that's packaged with PyQt
        'self' being passed is similar to setting a root node in katana - it parents the button the UI window created by the super()
        '''
        button = QPushButton("push me!", self)
        button.clicked.connect(self.buttonClicked) # when button is clicked, call the buttonClicked function
        button.move(80, 70)

    def buttonClicked(self):
        numberLabel = QLabel(self)
        if self.buttonClicked == True:
            numberLabel.setText()

app = QApplication(sys.argv)

myWindow = buttonWindow()
sys.exit(app.exec_())


    