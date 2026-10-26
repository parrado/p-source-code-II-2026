from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class window(QWidget):
   def __init__(self):
      super().__init__()
      self.resize(200,50)
      self.setWindowTitle("My first Window")
      self.label = QLabel(self)
      self.label.setText("Hello World")
      self.show()    

app = QApplication([])
ex = window()
app.exec()