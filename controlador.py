from PyQt5.QtWidgets import QApplication
from modelo import Modelo
from vista import Base
from vista import Visualizador
from vista import Host
import sys

class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def img_conextion(self, imagen,size=None):
       self.modelo.picture_creator(imagen,size)

    def main():
        app = QApplication(sys.argv)
        modelo = Modelo()
        vista = Base()
        vista3 = Visualizador()
        mi_controlador=Controlador(modelo,vista3)
        vista3.addControler(mi_controlador)
        vista.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    Controlador.main()

