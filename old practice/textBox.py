from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

import sys

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Listenign 2 Paramore')

        self.label = QLabel()

        # type box where user can add text
        self.input = QLineEdit()
        # anything typed in the above box is added to the widget
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = mainWindow()
window.show()

app.exec()