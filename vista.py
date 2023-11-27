from PyQt5.QtWidgets import QMainWindow, QSlider, QWidget, QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
#from os import listdir,
#from os.path import listdir, join

import os

class Vista(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('base.ui', self)

    #def leer_imagenesUI(imagenes_dieseño_ui):
       # images = [f for f in listdir(imagenes_dieseño_ui) if isfile(join(imagenes_dieseño_ui, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
       # return images

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
        #self.hide()
        # validar para abrir
        abrir_host.show()

class Host(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("host.ui", self)
        #self.__ventanaPadre = parent
        self.botones()

    def botones(self):
        self.cerrar_sesion.clicked.connect(self.abrir_base)
        self.boton10.clicked.connect(self.abrir_visualizador)
        self.boton50.clicked.connect(self.abrir_visualizador)
        self.boton100.clicked.connect(self.abrir_visualizador)

    def abrir_base(self):
        abrir_base = Base(self)
        #self.hide()
        # validar para abrir
        abrir_base.show()

    def abrir_visualizador(self):
        abrir_visualizador = Visualizador(self)
        #self.hide()
        # validar para abrir
        abrir_visualizador.show()

class Visualizador(QWidget):
    def __init__(self,base=None):
        super().__init__(base)
        loadUi("Visualizador.ui",self)
        self.slider = QSlider(self)
        self.slider.setGeometry(400, 430, 221, 22)
        self.slider.setOrientation(0x1)
        self.__ventanaPadre = base
        self.setup()

    #def setup(self):
        #self.comboBox.currentIndexChanged.connect(self.cargar)
        #self.slider.valueChanged.connect(self.cargar)

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