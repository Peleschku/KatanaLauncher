# imports the widgets I need from PyQt5
from PyQt5.QtWidgets import QApplication, QWidget

import sys

# creates the application. sys.argv allows you to pass 
# cmd line arguments through the appliction
app = QApplication(sys.argv)

# making the window that opens when the application is
# launched

window = QWidget()
window.show()

# starts the application
app.exec()