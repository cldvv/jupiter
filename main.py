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
        

        #establishes connections between elements
        

        #sets the window appearance (label, size, location)
        

        # start:
        

    def initUI(self):
        ''' cream si initializam elementele grafice din interfata'''
    
    def next_click(self):
        '''next click place holder'''

    def connects(self):
        '''atasam la evenimentul de click al butonului next metoda asociata predefinita mai sus'''

    '''configuram modul in care va arata fereastra (titlu, marime, locatia pe ecran)'''
    def set_appear(self):
        '''setWindowTitle(...), resize(...),move(...)'''

app = QApplication([])
mw = MainWin()
app.exec_()
