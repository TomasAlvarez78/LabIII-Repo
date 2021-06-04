import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QGridLayout,QPushButton,QVBoxLayout,QLineEdit

#Clase contenedora de Calculadora
class PyCalculadora(QMainWindow):
	def __init__(self):
		#Llamo al constructor de la ventana normal
		super().__init__()
		#Seteo el nombre de la ventana
		self.setWindowTitle("Calculadora")
		#Seteo el tamano inicial
		self.setFixedSize(250,250)
		#Anado una capa Layout
		self.capa = QVBoxLayout()
		#Anado un widget para poner arriba de la capa Layout maestra
		self.widget = QWidget(self)
		self.setCentralWidget(self.widget)
		#Seteo el widget sobre la capa maestra
		self.widget.setLayout(self.capa)
		#Funciones de crear Display y Botones
		self.createDisplay()
		self.createButtons()

	def setDisplayText(self,text):
		self.display.setText(text)
		self.display.setFocus()

	def concatDisplayText(self,text):
		textIni = self.getdisplayText()
		textIni += text
		self.setDisplayText(textIni)

	def getdisplayText(self):
		return self.display.text()

	def clearDisplay(self):
		self.setDisplayText('')

	def createDisplay(self):
		#Seteo display como objeto
		self.display = QLineEdit()
		self.display.setFixedHeight(35)
		self.display.setAlignment(Qt.AlignRight)
		self.display.setReadOnly(True)
		#Anado a la capa maestra el widget recien creado
		self.capa.addWidget(self.display)

	def createButtons(self):
		self.botones = {}
		capaBotones = QGridLayout()
		buttons = {'7': (0, 0),'8': (0, 1),'9': (0, 2),'/': (0, 3),'C': (0, 4),
                   '4': (1, 0),'5': (1, 1),'6': (1, 2),'*': (1, 3),'(': (1, 4),
                   '1': (2, 0),'2': (2, 1),'3': (2, 2),'-': (2, 3),')': (2, 4),
                   '0': (3, 0),'00': (3, 1),'.': (3, 2),'+': (3, 3),'=': (3, 4),
		}
		for btnText, pos in buttons.items():
			self.botones[btnText] = QPushButton(btnText)
			self.botones[btnText].setFixedSize(40,40)
			capaBotones.addWidget(self.botones[btnText],pos[0],pos[1])

		#Asignacion de acciones a botones
		self.botones['7'].clicked.connect(lambda: self.buttonClick('7'))
		self.botones['8'].clicked.connect(lambda: self.buttonClick('8'))
		self.botones['9'].clicked.connect(lambda: self.buttonClick('9'))
		self.botones['/'].clicked.connect(lambda: self.buttonClick('/'))
		self.botones['C'].clicked.connect(lambda: self.buttonClick('C'))
		self.botones['4'].clicked.connect(lambda: self.buttonClick('4'))
		self.botones['5'].clicked.connect(lambda: self.buttonClick('5'))
		self.botones['6'].clicked.connect(lambda: self.buttonClick('6'))
		self.botones['*'].clicked.connect(lambda: self.buttonClick('*'))
		self.botones['('].clicked.connect(lambda: self.buttonClick('('))
		self.botones['1'].clicked.connect(lambda: self.buttonClick('1'))
		self.botones['2'].clicked.connect(lambda: self.buttonClick('2'))
		self.botones['3'].clicked.connect(lambda: self.buttonClick('3'))
		self.botones['-'].clicked.connect(lambda: self.buttonClick('-'))
		self.botones[')'].clicked.connect(lambda: self.buttonClick(')'))
		self.botones['0'].clicked.connect(lambda: self.buttonClick('0'))
		self.botones["00"].clicked.connect(lambda: self.buttonClick("00"))
		self.botones['.'].clicked.connect(lambda: self.buttonClick('.'))
		self.botones['+'].clicked.connect(lambda: self.buttonClick('+'))
		self.botones['='].clicked.connect(lambda: self.buttonClick('='))
		#Anado la capa de botones (gridLayout) a la capa maestra
		self.capa.addLayout(capaBotones)

	def buttonClick(self, button):
		if(button == 'C'):
			self.clearDisplay()
		elif(button == '='):
			self.resultado()
		else:
			self.concatDisplayText(button)

	def resultado(self):
		try:
			res = float(eval(self.getdisplayText()))
		except ZeroDivisionError:
			self.setDisplayText("ERROR")
		if(res.is_integer()):
			self.setDisplayText(str(int(res)))
		else:
			self.setDisplayText(str(res))
		print(res)

def main():
	pyCalculadora = QApplication(sys.argv)
	calcu = PyCalculadora()
	calcu.show()
	sys.exit(pyCalculadora.exec())

if __name__ == '__main__':
	main()