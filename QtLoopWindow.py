import sys

# imports the widgets I need from PyQt5
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

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
        self.button.setCheckable(True)
        self.button.released.connect(self.buttonWasReleased)
        self.buttonIsChecked = False
        self.button.setChecked(self.buttonIsChecked)

        # centers the button on the window
        # button created above is passed through as an argument
        self.setCentralWidget(self.button)

    #functions containting the thing that happens when the button was clicked
    
    def buttonWasReleased(self):
        self.buttonIsChecked = self.button.isChecked()

        print(self.buttonIsChecked)



# creates the application. sys.argv allows you to pass
# cmd line arguments through the appliction
app = QApplication(sys.argv)

# making the window that opens when the application is launched

window = mainWindow()
window.show()


# starts the application
app.exec()
