from fabricas import *
from heroe import *

class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getHeroe(self,id):
        heroe = Heroe(id)
        heroe.set_sprites(self.__builder.get_sprites())
        heroe.set_mensajes(self.__builder.get_mensajes())

        return heroe

class Constructor():
    def get_sprites(self):
        return [self.fabrica.crear_derecha(),
                self.fabrica.crear_izquierda(),
                self.fabrica.crear_abajo(),
                self.fabrica.crear_arriba()]

    def get_mensajes(self): pass

class ConstructorHumanos(Constructor):
    def __init__(self):
        self.fabrica = FabricaSpritesHumano()

    def get_mensajes(self):
        return ["todo bien", "ayudaaa", "cambia de direccion"]

class ConstructorEsqueletos(Constructor):
    def __init__(self):
        self.fabrica = FabricaSpritesEsqueleto()

    def get_mensajes(self):
        return ["jajajaj", "apurate", "gira"]

class ConstructorZombis(Constructor):
    def __init__(self):
        self.fabrica = FabricaSpritesZombi()

    def get_mensajes(self):
        return ["aaaaa", "eeeeeeee", "iiiiii"]
