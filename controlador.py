from PyQt5.QtWidgets import QApplication
from modelo import Modelo
from vista import Base
import sys

class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def img_conextion(self, imagen):
       self.modelo.picture_creator(imagen)

    def main():
        app = QApplication(sys.argv)
        modelo = Modelo()
        vista = Base()
        mi_controlador=Controlador(modelo,vista)
        #vista.addControler(mi_controlador)
        vista.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    Controlador.main()

