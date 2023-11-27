from PyQt5.QtWidgets import QMainWindow, QSlider, QForm
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi

import os

class Vista(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('base.ui', self)
        self.slider = QSlider(self)
        self.slider.setGeometry(400, 430, 221, 22)
        self.slider.setOrientation(0x1)

    def setup(self):
        self.comboBox.currentIndexChanged.connect(self.cargar)
        self.slider.valueChanged.connect(self.cargar)

        self.carpeta = 'images10'
        lista_archivos = os.listdir(self.carpeta)
        self.slider.setMaximum(len(lista_archivos) - 1)  # Establece el valor máximo del slider

        for archivo in lista_archivos:
            self.comboBox.addItem(archivo)

    def addControler(self, c):
        self.__mi_coordinador = c
        self.setup()

    def cargar(self):
        index = self.slider.value()
        imagen = self.comboBox.itemText(index)
        self.__mi_coordinador.img_conextion(imagen)

        pixmap = QPixmap("temp_image.png")
        self.img.setPixmap(pixmap)
        os.remove('temp_image.png')

class Base(QMainWindow):
    def __init__(self,base=None):
        super().__init__(base)
        loadUi("base.ui",self)
        # crear validacion
        #self.__usuario: "medicoAnalitico"
        #self.__contraseña: "bio12345"
        self.botones()

    def botones(self):
        self.iniciar_sesion.clicked.connect(self.abrir_host)

    def abrir_host(self):
        abrir_host = Host(self)
        # validar para abrir
        Host.show()

class Host(QMainWindow):
    def __init__(self,base=None):
        super().__init__(base)
        loadUi("Host.ui",self)
        self.botones()

class Visualizador(QForm):
    def __init__(self,base=None):
        super().__init__(base)
        loadUi("Visualizador.ui",self)
        self.botones()