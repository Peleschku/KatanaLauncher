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
        self.path = "variables.json"
        self.createTable()
        
    
    def createTable(self):

        self.my_env = {}
        
        if (os.path.exists(self.path)):
            print("Found path!")

            with open(self.path) as env_json:
                self.my_env = json.load(env_json)
        else:
            self.my_env = dict(os.environ)
            with open(self.path, "w") as env_json: 
                json.dump(self.my_env , env_json, indent=2)
        
        print(self.my_env)

            
        self.setGeometry(150, 250, 250, 300)
        self.setWindowTitle('Pls work table')

        layout = QGridLayout()

        self.data = QTableWidget()
        self.data.setColumnCount(2)

        self.data.horizontalHeader().setStretchLastSection(True)
        self.data.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        

        for self.key, self.value in self.my_env.items():
            self.data.insertRow(self.data.rowCount())
            self.data.setItem(self.data.rowCount() - 1, 0, QTableWidgetItem(self.key))
            self.data.setItem(self.data.rowCount() - 1, 1, QTableWidgetItem(self.value))

        


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

        self.saveVariablesBttn = QPushButton("Save Variables")
        self.saveVariablesBttn.clicked.connect(self.saveVariablesOut)

        self.currentRow = -1

        
        layout.addWidget(self.data, 1, 0, 1, 4)
        layout.addWidget(variableName, 2, 0)
        layout.addWidget(variableValue, 2, 2)
        layout.addWidget(self.setVariableName, 3, 0)
        layout.addWidget(self.setVariableNameBttn, 3, 1)
        layout.addWidget(self.setVariableValue, 3, 2)
        layout.addWidget(self.setVariableValueBttn, 3, 3)
        layout.addWidget(self.deleteRowBttn, 4, 0, 1, 4)
        layout.addWidget(self.saveVariablesBttn, 5, 0, 1, 4)


        self.setLayout(layout)
        self.show()

    def addVariableName(self):
        
        nameText = self.setVariableName.text()

        self.data.insertRow(self.data.rowCount())
        
        # counts how many rows there are and then -1 to get the index of the row
        # and not the UI's count of the row (0 indexing and all that)
        
        self.data.setItem(self.data.rowCount() - 1, 0, QTableWidgetItem(nameText))


    def addVariableValue(self):
        valueText = self.setVariableValue.text()

        self.data.setItem(self.data.rowCount() - 1, 1, QTableWidgetItem(valueText))
        
    
    def deleteSelectedRow(self):
        selected = self.data.currentRow()

        self.data.removeRow(selected)

    def saveVariablesOut(self):
                  
        keys = []

        
        for keyRows in range(self.data.rowCount()):
            nameItems = self.data.item(keyRows, 0)
            keys.append(nameItems.text())
            

        values = []

        for valueRows in range(self.data.rowCount()):
            nameItems = self.data.item(valueRows, 1)
            values.append(nameItems.text())
        

        variablesDictionary = dict(zip(keys, values))

        print(variablesDictionary)



        with open('variables.json', 'w') as jsonfile:
            json.dump(variablesDictionary, jsonfile, indent=2)

    

app = QApplication(sys.argv)

window = tableTest()

sys.exit(app.exec_())