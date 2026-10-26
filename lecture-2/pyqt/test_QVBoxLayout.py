from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self,size):
        super().__init__()

        self.resize(size.width(), size.height())
        self.setWindowTitle("Vertical layout")
       
        # Se crean los botones
        redButton=QPushButton('red')
        greenButton=QPushButton('green')
        blueButton=QPushButton('blue')

        # Se cambia el color de los botones
        redButton.setStyleSheet("background-color: red")
        greenButton.setStyleSheet("background-color: green")
        blueButton.setStyleSheet("background-color: blue")

        # Se crea un layout vertical
        layout = QVBoxLayout()
        # Se añaden los widgets al layout
        layout.addWidget(redButton)
        layout.addWidget(greenButton)
        layout.addWidget(blueButton)

        widget = QWidget()
        widget.setLayout(layout)
        #QMainWindow requiere un widget central
        self.setCentralWidget(widget)

        
        # Deshabilita el botón de maximizar
        self.setWindowFlags( Qt.MSWindowsFixedSizeDialogHint)

app = QApplication([])
screen = app.primaryScreen()
size = screen.size()
       
ex = MainWindow(size)
ex.show()
app.exec()