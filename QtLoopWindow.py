import sys

# imports the widgets I need from PyQt5
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Setting the text that appears in the top bar
        # of the window
        self.setWindowTitle("Adele's App!")
        
        # creates the button and adds text to it
        button = QPushButton("Press Me!")
        
        # centers the button on the window
        # button created above is passed through as an argument
        self.setCentralWidget(button)

# creates the application. sys.argv allows you to pass 
# cmd line arguments through the appliction
app = QApplication(sys.argv)

# making the window that opens when the application is
# launched

window = mainWindow
window.show() # this line is breaking soemthing, need to check it later.

# starts the application
app.exec()