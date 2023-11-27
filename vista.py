from PyQt5.QtWidgets import QMainWindow, QSlider, QWidget, QDialog,QComboBox
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from modelo import DataBase
from modelo import Modelo
#from controlador import Controlador
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
    
    def obtenerNew(self):
        host = Host()
        return host.retornar()

class Host(QDialog):
    def __init__(self, base=None):
        super().__init__(base)
        loadUi("host.ui", self)
        self.ventanaPadre = base
        self.vista= ""
        self.botones()

    def botones(self):
        self.cerrar_sesion.clicked.connect(self.abrir_base)
        self.boton10.clicked.connect(self.abrir_visualizador10)
        self.boton50.clicked.connect(self.abrir_visualizador50)
        self.boton100.clicked.connect(self.abrir_visualizador100)

    def abrir_base(self):
        abrir_base = Base(self)
        self.hide()
        abrir_base.show()

    def abrir_visualizador10(self):
        modelo =Modelo()

        abrir_visualizador = Visualizador(self,size=10)
        self.vista = abrir_visualizador
       
        self.hide()
        # validar para abrir
        abrir_visualizador.show()
    

    def retornar(self):
        return self.vista
    
    def abrir_visualizador50(self):
        modelo =Modelo()
        abrir_visualizador = Visualizador(self,size=50)
        self.vista = abrir_visualizador
        self.hide()
        # validar para abrir
        abrir_visualizador.show()

    def abrir_visualizador100(self):
        modelo =Modelo()
        abrir_visualizador = Visualizador(self,size=100)
        self.vista = abrir_visualizador
        
        self.hide()
        # validar para abrir
        abrir_visualizador.show()
        
    def abrir_host(self):
        abrir_host = Host(self)
        self.hide()
        if DataBase is False:
            login = self.linea_usuario.text()
            password = self.linea_contrasena.text()
            print("Ingreso exitoso...")
            abrir_host.show()
        else:
            abrir_host.show()
            pass

class Visualizador(QDialog):
    def __init__(self,Base=None,size=None):
        super().__init__(Base)
        loadUi("Visualizador.ui",self)
        self.slider = QSlider(self)
        self.slider.setGeometry(400, 430, 221, 22)
        self.slider.setOrientation(0x1)
        self.comboBox = QComboBox(self)
        self.ventanaPadre = Base
        self.size = size
        self.botones()

    def botones(self):
        self.cerrar_sesion.clicked.connect(self.abrir_base)
        self.atras.clicked.connect(self.abrir_host)

    def abrir_base(self):
        abrir_base = Base(self)
        self.hide()
        abrir_base.show()

    def abrir_host(self):
        abrir_host = Host(self)
        self.hide()
        # validar para abrir
        abrir_host.show()
        #self.setup()

    def setup(self):
        self.comboBox.currentIndexChanged.connect(self.cargar)
        self.slider.valueChanged.connect(self.cargar)
         
        if self.size != None:
            self.carpeta = 'images'+str(self.size)
        else:
            self.carpeta = 'images10'
        lista_archivos = os.listdir(self.carpeta)
        
        self.slider.setMaximum(len(lista_archivos) - 1) 
        self.comboBox.setVisible(False)

        for archivo in lista_archivos:
                self.comboBox.addItem(archivo)

    def addControler(self, c):
        self.__mi_coordinador = c
        self.setup()

    def cargar(self):
        index = self.slider.value()
        imagen = self.comboBox.itemText(index)
        self.__mi_coordinador.img_conextion(imagen,self.size)

        pixmap = QPixmap("temp_image.png")
        self.img.setPixmap(pixmap)
        os.remove('temp_image.png')