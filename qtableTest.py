import sys
import os
from os.path import isfile, join
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class tableTest(QWidget):
    def __init__(self):
        super().__init__()
        self.createTable()

    def createTable(self):

        self.setGeometry(150, 250, 250, 300)
        self.setWindowTitle('Pls work table')

        layout = QGridLayout()

        self.data = QTableWidget()
        self.data.setColumnCount(2)

        self.data.horizontalHeader().setStretchLastSection(True)
        self.data.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        variableName = QLabel('Set Variable Name')
        self.setVariableName = QLineEdit()
        self.setVariableNameBttn = QPushButton('Set')
        self.setVariableNameBttn.clicked.connect(self.addVariableName)

        variableValue = QLabel('Set Variable Value')
        self.setVariableValue = QLineEdit()
        self.setVariableValueBttn = QPushButton('Set')
        self.setVariableValueBttn.clicked.connect(self.addVariableValue)

        self.currentRow = -1

        layout.addWidget(self.data, 1, 0, 1, 4)
        layout.addWidget(variableName, 2, 0)
        layout.addWidget(variableValue, 2, 2)
        layout.addWidget(self.setVariableName, 3, 0)
        layout.addWidget(self.setVariableNameBttn, 3, 1)
        layout.addWidget(self.setVariableValue, 3, 2)
        layout.addWidget(self.setVariableValueBttn, 3, 3)





        self.setLayout(layout)
        self.show()

    def addVariableName(self):
        nameText = self.setVariableName.text()

        # appends 1 to the current row (prevents values being pasted on top of each other)
        self.currentRow += 1
        
        # if the current row is larger than the rows currently in the table, add a new one 
        if self.currentRow > self.data.rowCount() -1:
            self.data.insertRow(self.data.rowCount())
        
        # add the text in the QLineEdit to the row that was created in the above if statement
        self.data.setItem(self.currentRow, 0, QTableWidgetItem(nameText))
        print(nameText)

    def addVariableValue(self):
        valueText = self.setVariableValue.text()

        '''
        self.currentRow += 1
        
        if self.currentRow > self.data.rowCount() -1:
            self.data.insertRow(self.data.rowCount())
        '''
        self.data.setItem(self.currentRow, 1, QTableWidgetItem(valueText))


        print(valueText)
    

app = QApplication(sys.argv)

window = tableTest()

sys.exit(app.exec_())