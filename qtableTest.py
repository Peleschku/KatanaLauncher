import sys
import os
from os.path import isfile, join
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import json

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

        self.deleteRowBttn = QPushButton("Delete Selected Row")
        self.deleteRowBttn.clicked.connect(self.deleteSelectedRow)

        self.currentRow = -1

        
        layout.addWidget(self.data, 1, 0, 1, 4)
        layout.addWidget(variableName, 2, 0)
        layout.addWidget(variableValue, 2, 2)
        layout.addWidget(self.setVariableName, 3, 0)
        layout.addWidget(self.setVariableNameBttn, 3, 1)
        layout.addWidget(self.setVariableValue, 3, 2)
        layout.addWidget(self.setVariableValueBttn, 3, 3)
        layout.addWidget(self.deleteRowBttn, 4, 0, 1, 4)


        self.setLayout(layout)
        self.show()

    def addVariableName(self):
        
        nameText = self.setVariableName.text()

        self.data.insertRow(self.data.rowCount())
        
        # counts how many rows there are and then -1 to get the index of the row
        # and not the UI's count of the row (0 indexing and all that)
        
        self.data.setItem(self.data.rowCount() - 1, 0, QTableWidgetItem(nameText))

        print(nameText)

    def addVariableValue(self):
        valueText = self.setVariableValue.text()

        self.data.setItem(self.data.rowCount() - 1, 1, QTableWidgetItem(valueText))


        print(valueText)
    
    def deleteSelectedRow(self):
        selected = self.data.currentRow()

        self.data.removeRow(selected)
    

app = QApplication(sys.argv)

window = tableTest()

sys.exit(app.exec_())