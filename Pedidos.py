class Clase_Pedido:
    __PatenteAsig: str
    __IdentificadorP: int 
    __CantComidas: int
    __TiempoEntrega:int
    __Tiemporeal: float
    __Precio: float 

    def __init__(self, patente, identificador, comidas, entrega, real, precio):
        self.__PatenteAsig= patente
        self.__IdentificadorP= identificador
        self.__CantComidas= comidas
        self.__TiempoEntrega= entrega
        self.__Tiemporeal= real 
        self.__Precio= precio

    def getPatenteasig (self):
        return self.__PatenteAsig
    
    def getIdentificador (self):
        return self.__IdentificadorP

    def getComidas (self):
        return self.__CantComidas

    def getTiempodeEntrega (self):
        return self.__TiempoEntrega

    def getTiempoReal (self):
        return self.__Tiemporeal

    def getPrecio (self):
        return self.__Precio
    
    def ModificarT (self, t):
        self.__Tiemporeal=t

    def __it__ (self, other):
        return self.__PatenteAsig<other.__PatenteAsig

    def __gt__ (self, other):
        return self.__PatenteAsig>other.__PatenteAsig