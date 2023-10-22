# https://realpython.com/python-pyqt-gui-calculator/#creating-your-first-pyqt-application

from PyQt5.QtWidgets import (QApplication, 
                             QLabel,
                             QWidget,
                             QMainWindow,
                             QHBoxLayout,
                             QPushButton,
                             QWidget,
                             )

import sys

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('help pls')
        self.setGeometry(100, 100, 280, 80)

        self.layout = QHBoxLayout
        #self.layout.addWidget(QPushButton("Left"))
        self.layout.addWidget(QPushButton("Center"))
        self.layout.addWidget(QPushButton("Right"))

        self.setLayout(self.layout)

        #self.helloMsg = QLabel('<h1>Hello, World!</h1>', parent=self)
        #self.helloMsg.move(60, 15)

        #self.setCentralWidget(self.helloMsg)
        


app = QApplication(sys.argv)

window = mainWindow()
window.show()

app.exec()