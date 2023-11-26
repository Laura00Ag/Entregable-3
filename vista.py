from PyQt5.QtWidgets import QMainWindow, QSlider
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi

import os

class Vista(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('base.ui', self)
        self.slider = QSlider(self)
        self.slider.setGeometry(10, 400, 380, 20)  # Ajusta la geometría según tus necesidades
        self.slider.setOrientation(0x1)  # Configura la orientación horizontal

    def setup(self):
        self.comboBox.currentIndexChanged.connect(self.cargar)
        self.slider.valueChanged.connect(self.cargar)

        self.carpeta = 'images'
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
