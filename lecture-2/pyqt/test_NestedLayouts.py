from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nested layouts")
       
        # Se crean los botones
        redButton=QPushButton('red')
        greenButton=QPushButton('green')
        blueButton=QPushButton('blue')
        whiteButton=QPushButton('white')
        brownButton=QPushButton('brown')

        # Se cambia el color de los botones
      
        redButton.setStyleSheet("background-color: red")
        greenButton.setStyleSheet("background-color: green")
        blueButton.setStyleSheet("background-color: blue")
        whiteButton.setStyleSheet("background-color: white")
        brownButton.setStyleSheet("background-color: brown")
       
        # Se crea un layout horizontal
        hLayout = QHBoxLayout()
        # Se añaden los widgets al layout
        hLayout.addWidget(redButton)
        hLayout.addWidget(greenButton)
        hLayout.addWidget(blueButton)

        # Se crea un layout vertical
        vLayout = QVBoxLayout()
        # Se añaden los widgets al layout
        vLayout.addWidget(whiteButton)
        vLayout.addWidget(brownButton)
        frame=QWidget()
        frame.setLayout(vLayout)
        
        hLayout.addWidget(frame)



        widget = QWidget()
        widget.setLayout(hLayout)
        #QMainWindow requiere un widget central
        self.setCentralWidget(widget)

        
        # Deshabilita el botón de maximizar
        self.setWindowFlags( Qt.MSWindowsFixedSizeDialogHint)

app = QApplication([])
ex = MainWindow()
ex.show()
app.exec()