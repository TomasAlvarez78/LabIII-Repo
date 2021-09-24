import sys
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication,QMainWindow,QWidget,QGridLayout,QPushButton,QVBoxLayout,QLineEdit,QLabel
from graficoplotly import *

class PyMain(QMainWindow):
    def __init__(self):
        super().__init__()

        self.graficoBarra = GraficoBarra()
        self.graficoBarra.requestAPI()

        self.setWindowTitle("Aplicacion Lab III")
        self.setFixedSize(382,230)

        # Creo los Layouts
        self.capaVertical = QVBoxLayout()
        self.capaGrid = QGridLayout()
        self.capaButtons = QVBoxLayout()
        
        # Creo el Main Layout
        self.mainLayout = QVBoxLayout()

        # Creo un widget principal y lo agrego al Main Layout
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.widget.setLayout(self.mainLayout)

        # Funciones de Creacion de Objetos
        self.createImage()
        # self.createText()
        # self.createDisplay()
        self.createButtons()

        self.capaVertical.addStretch(1)
        self.capaButtons.addStretch(1)

        self.mainLayout.addLayout(self.capaVertical)
        self.mainLayout.addLayout(self.capaGrid)
        self.mainLayout.addLayout(self.capaButtons)

    def createImage(self):
        label = QLabel(self)
        pixmap = QPixmap('img/banner.png')
        label.setPixmap(pixmap)
        self.capaVertical.addWidget(label)

    def createText(self):
        text = QLabel("Minimo: ")
        text2 = QLabel("Maximo: ")
        text.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        text2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font = text.font()
        font.setPointSize(12)
        text.setFont(font)
        text2.setFont(font)
        self.capaGrid.addWidget(text,1,0)
        self.capaGrid.addWidget(text2,2,0)

    def createDisplay(self):
        self.display = QLineEdit()
        self.display2 = QLineEdit()

        self.display.setFixedHeight(35)
        self.display2.setFixedHeight(35)

        self.display.setAlignment(Qt.AlignRight)
        self.display2.setAlignment(Qt.AlignRight)

        self.capaGrid.addWidget(self.display,1,1)
        self.capaGrid.addWidget(self.display2,2,1)

    def createButtons(self):
        # button1 = QPushButton("Request API")        
        # button1.clicked.connect(self.runAPI)

        button2 = QPushButton("Top 10 menos muertes")        
        button2.clicked.connect(self.menosMuertes)

        button3 = QPushButton("Top 10 mas muertes")        
        button3.clicked.connect(self.masMuertes)

        # self.capaButtons.addWidget(button1)
        self.capaButtons.addWidget(button2)
        self.capaButtons.addWidget(button3)

    def runAPI(self):
        self.graficoBarra = GraficoBarra()
        self.graficoBarra.requestAPI()

    def menosMuertes(self):
        self.graficoBarra.graficarMenor()

    def masMuertes(self):
        self.graficoBarra.graficarMayor()



