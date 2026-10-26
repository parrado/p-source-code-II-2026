from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(320,240)

        self.setWindowTitle("Click button example")
       
        
        
        self.l1=QLabel('Etiqueta')
        self.b1=QPushButton('Botón')

        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.l1.setFont(font)
        self.b1.setFont(font)

        
        # Conecta señal 'clicked' a slot onClick
        self.b1.clicked.connect(self.onClick)

       
        # Se crea un layout de cuadrícula
        gridLayout=QGridLayout()
        # Se añaden los widgets al layout
        gridLayout.addWidget(self.l1,0,0,alignment=Qt.AlignCenter)
        gridLayout.addWidget(self.b1,1,0)
        
      
        # Crea el widget central
        widget = QWidget()
        widget.setLayout(gridLayout)       


        
        #QMainWindow requiere un widget central
        self.setCentralWidget(widget)

        
        # Deshabilita el botón de maximizar
        self.setWindowFlags( Qt.MSWindowsFixedSizeDialogHint)
    
    def onClick(self):
        print('Click')       
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Cuadro de mensaje emergente")
        msgBox.setWindowTitle("QMessageBox Example")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ret=msgBox.exec()
        print(ret)
        if ret==2**10:
            print('Presionaste OK')
            self.l1.setText("Texto cambiado")
        if ret==2**22:
            print('Presionaste Cancel')

app = QApplication([])
ex = MainWindow()
ex.show()
app.exec()