class TV:
    _numTV = 0

    def __init__(self, marca, estado):
        self.__marca = marca
        self.__estado = estado
        self.__canal = 1
        self.__precio = 500
        self.__volumen = 1
        self.__control = None
        TV._numTV += 1

    def setMarca(self, marca):
        self.__marca = marca

    def getMarca(self):
        return self.__marca

    def setControl(self, control):
        self.__control = control

    def getControl(self):
        return self.__control

    def setPrecio(self, precio):
        self.__precio = precio

    def getPrecio(self):
        return self.__precio

    def setVolumen(self, volumen):
        if 0 <= volumen <= 7:
            self.__volumen = volumen

    def getVolumen(self):
        return self.__volumen

    def setCanal(self, canal):
        if 1 <= canal <= 120:
            self.__canal = canal

    def getCanal(self):
        return self.__canal

    def turnOn(self):
        self.__estado = True

    def turnOff(self):
        self.__estado = False

    def canalUp(self):
        if self.__estado and self.__canal < 120:
            self.__canal += 1

    def canalDown(self):
        if self.__estado and self.__canal > 1:
            self.__canal -= 1

    def volumenUp(self):
        if self.__estado and self.__volumen < 7:
            self.__volumen += 1

    def volumenDown(self):
        if self.__estado and self.__volumen > 0:
            self.__volumen -= 1

    @classmethod
    def getNumTV(cls):
        return cls._numTV

    @classmethod
    def setNumTV(cls, numTV):
        cls._numTV = numTV
