from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

#from instr import *
#from second_win import *

       
class MainWin(QWidget):
    def __init__(self):
        ''' the window which the greeting is located in '''
        super().__init__()

        # creating and configuring graphic elements:
        self.initUI()

        #establishes connections between elements
        self.connects()

        #sets the window appearance (label, size, location)
        self.set_appear()

        # start:
        self.show()

    def initUI(self):
        ''' creates graphic elements '''
    
    def next_click(self):
        '''next click place holder'''

    def connects(self):
        pass

    ''' sets what the window will look like (label, size, location) '''
    def set_appear(self):
        print(3)

app = QApplication([])
mw = MainWin()
app.exec_()
