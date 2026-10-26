from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test other widgets")
       
        self.lw = QListWidget()
        self.lw.insertItem(0, "Python")
        self.lw.insertItem(1, "Java")
        self.lw.insertItem(2, "Kotlin")
        self.lw.insertItem(3, "Rust")

        self.rb1=QRadioButton("English")
        self.rb2=QRadioButton("German")
        self.rb3=QRadioButton("French")

        pixmap = QPixmap(400, 300)
        pixmap.fill(Qt.white)

        self.canvas=QLabel()
        self.canvas.setPixmap(pixmap)

        layout=QGridLayout()

        layout.addWidget(self.lw,0,0,4,1)

        layout.addWidget(self.rb1,0,1)
        layout.addWidget(self.rb2,1,1)
        layout.addWidget(self.rb3,2,1)

        layout.addWidget(self.canvas,4,0,3,2)
        

        widget = QWidget()
        widget.setLayout(layout)
        #QMainWindow requiere un widget central
        self.setCentralWidget(widget)

        
        # Deshabilita el botón de maximizar
        self.setWindowFlags( Qt.MSWindowsFixedSizeDialogHint)

        self.drawCircle()

    def drawCircle(self):
        painter=QPainter(self.canvas.pixmap())
        painter.setBrush(QBrush(QColor("red")))
        painter.setPen(QPen(QColor("blue")))
        painter.drawEllipse(200-30,150-30,60,60)
        painter.end()


app = QApplication([])
ex = MainWindow()
ex.show()
app.exec()