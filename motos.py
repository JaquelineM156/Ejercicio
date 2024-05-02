class Clase_Motos:
    def __init__ (self, patente, marca, nomyap, kilometraje):
        self.__Patente= patente
        self.__Marca= marca
        self.__NyA= nomyap
        self.__Kilometraje= kilometraje

    def getPatente (self):
        return self.__Patente
    
    def getMarca (self):
        return self.__Marca
    
    def getNyA (self):
        return self.__NyA
    
    def getKilometraje (self):
        return self.__Kilometraje
