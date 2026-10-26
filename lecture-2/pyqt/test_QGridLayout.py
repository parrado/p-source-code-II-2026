from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid layout")
       
        # Se crean los labels
        l1=QLabel('Height')
        l2=QLabel('Width')

        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        l1.setFont(font)
        l2.setFont(font)

        # Se crean los campos de entrada
        e1=QLineEdit()
        e2=QLineEdit()

        # Se crean el botón de chequeo
        c1=QCheckBox("Preserve")


        # Se crea un layout de cuadrícula
        gridLayout=QGridLayout()
        # Se añaden los widgets al layout
        gridLayout.addWidget(l1,0,0)
        gridLayout.addWidget(l2,1,0)
        
        gridLayout.addWidget(e1,0,1)
        gridLayout.addWidget(e2,1,1)
        
        # c1 ocupa una fila y dos columnas
        gridLayout.addWidget(c1,2,0,1,2)

        # Se crea un label para mostrar la imagen
        image = QLabel(self)        
        # Abre la imagen
        pixmap=QPixmap("pyqt/kratos.png")        
        # Asigna la imagen al pixmap, antes reduciendo el tamaño 
        image.setPixmap(pixmap.scaled(int(pixmap.width()/2),int(pixmap.height()/2)))
        # image ocupa dos filas y dos columnas
        gridLayout.addWidget(image,0,2,2,2)

        # Crea el widget central
        widget = QWidget()
        widget.setLayout(gridLayout)       


        
        #QMainWindow requiere un widget central
        self.setCentralWidget(widget)

        
        # Deshabilita el botón de maximizar
        self.setWindowFlags( Qt.MSWindowsFixedSizeDialogHint)

app = QApplication([])
ex = MainWindow()
ex.show()
app.exec()