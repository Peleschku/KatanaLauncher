import sys

# imports the widgets I need from PyQt5
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice

windowTitles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on Earth',
    'What on Earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # setting window size
        self.setFixedSize(300, 200)

        # Setting the text that appears in the top bar
        # of the window
        self.setWindowTitle("Adele's App!")
        
        # creates the button and adds text to it
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.buttonWasClicked)

        self.windowTitleChanged.connect(self.theWindowTitleChanged)

        # centers the button on the window
        # button created above is passed through as an argument
        self.setCentralWidget(self.button)

    #functions containting the thing that happens when the button was clicked
    def buttonWasClicked(self):
        print('Clicked.')
        newWindowTitle = choice(windowTitles)
        print('Setting title: %s' % windowTitles)
        self.setWindowTitle(newWindowTitle)

    def theWindowTitleChanged(self, windowTitle):
        print('Window title changed: %s' % windowTitle)

        if windowTitle == 'Something went wrong':
            self.button.setDisabled(True)


# creates the application. sys.argv allows you to pass
# cmd line arguments through the appliction
app = QApplication(sys.argv)

# making the window that opens when the application is launched

window = mainWindow()
window.show()


# starts the application
app.exec()
