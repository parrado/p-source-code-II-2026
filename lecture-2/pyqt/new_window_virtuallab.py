from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from virtuallab_client import *
from json import loads
import zipfile
from PySpice.Unit import *
from PySpice.Spice.Parser import SpiceParser
from virtuallab_client import *

# New window module for the virtual lab application. 
# This module defines a new window that allows users 
# to download and run virtual lab simulations. 
# The window displays a circuit image and provides
# buttons to request and run the lab.
# The simulation results are printed in the console.
#
# Alexander López Parrado, 2026

# Custom QLabel class that emits a signal when clicked
class ClickableImageLabel(QLabel):

  # Custom signal that emits (x, y) coordinates on the label
  clicked = pyqtSignal(int, int)
  

  def __init__(self, parent=None):
    super().__init__(parent)
    self.setMouseTracking(True)
    
  def mousePressEvent(self, event):
    if event.button() == Qt.MouseButton.LeftButton:
      pos = event.pos()
      self.clicked.emit(pos.x(), pos.y())
    super().mousePressEvent(event)

# Main window class inheriting from QMainWindow
# constructor takes the student ID as an argument
class NewWindow(QMainWindow):
    def __init__(self,id_student):
        super().__init__()
        self.id_student=id_student       
        self.setWindowTitle(f'Virtual Lab - Student ID: {self.id_student}')

        # analysis attribute is initialized to None, it will hold the simulation results after running the lab
        self.analysis = None  

        self.display_width = 640
        self.display_height = 480
        # Label to display lab circuit image
        self.image_label =  ClickableImageLabel()
        # Connect the clicked signal of the image label to the onCircuitClicked slot
        self.image_label.clicked.connect(self.onCircuitClicked)
       
        # Buttons to download and run the lab are created, 
        # with the run button initially disabled until a lab is downloaded
        button1=QPushButton('Solicitar laboratorio')
        button1.clicked.connect(self.downloadLab)                               

        self.button2=QPushButton('Correr laboratorio')
        self.button2.setEnabled(False)  
        self.button2.clicked.connect(self.runLab)

        # We create a grid layout to arrange the widgets in a grid format
        layout=QGridLayout()

        layout.addWidget(self.image_label, 0, 0, 2, 2)
        layout.addWidget(button1, 2, 0)
        layout.addWidget(self.button2, 2, 1) 

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)


    # Slot function to download the lab file from the server, 
    # extract them, and display the circuit image
    def downloadLab(self):        
        # Descarga laboratorio
        self.lab_name="voltage_divider"
        file_name=self.lab_name+".zip"
        url="http://127.0.0.1:80"
        print(downloadLab(url,self.id_student,file_name))
        # Open the downloaded zip file and extract the circuit image
        # and netlist
        with zipfile.ZipFile(f"client/labs/{file_name}", "r") as zip_ref:
            with zip_ref.open(self.lab_name+".png") as file:
                ba = QByteArray(file.read())
                pixmap=QPixmap()        
                pixmap.loadFromData(ba, "PNG")                
                # Asigna la imagen al pixmap, antes reduciendo el tamaño 
                self.image_label.setPixmap(pixmap.scaled(int(pixmap.width()/2),int(pixmap.height()/2)))                            
                self.image_label.resize(self.display_width, self.display_height)
            with zip_ref.open(self.lab_name+".cir") as file:        
                self.netlist = file.read().decode("utf-8")

            # As the lab has been downloaded and the circuit image
            # is displayed, we enable the run button
            self.button2.setEnabled(True)  

    # Slot function to run the lab simulation using PySpice
    def runLab(self):             
        print("Starting simulation for lab:", self.lab_name)
        # Crea un objeto SpiceParser a partir del contenido del archivo .cir
        parser = SpiceParser(source=self.netlist)
        # Crea el circuito a partir del parser
        circuit = parser.build_circuit()
        # Crea una instancia del simulador para ejecutar el análisis
        simulator = circuit.simulator(temperature=25, nominal_temperature=25)
        # Ejecuta la simulación (punto de operación)
        self.analysis = simulator.operating_point()
        print("Simulation completed for lab:", self.lab_name)
            
    # Slot function to handle clicks on the circuit image, 
    # printing the coordinates of the click 
    def onCircuitClicked(self, x, y):
        print(f"Circuit clicked at: ({x}, {y})")
        # If the simulation has been run and analysis is available,
        # we print the voltages at each node     
        if self.analysis is not None:
            for node in self.analysis.nodes.values():
                print(f'Node {node}: {float(node[0]):.4f} V')
        


   