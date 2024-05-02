from motos import Clase_Motos
from Pedidos import Clase_Pedido
import csv

class ManejadorMotos:
    __ListaMotos:list
    def __init__ (self):
        self.__ListaMotos= []
    
    def CargarMotos (self):
        archivo=open('Motos.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            m= Clase_Motos(fila[0],fila[1],fila[2],float(fila[3]))
            self.__ListaMotos.append(m)
        archivo.close() 

    def Validar_Patente (self, patente):
        valor=0
        i=0
        while i <(len(self.__ListaMotos)):
            if patente == self.__ListaMotos[i].getPatente ():
                valor=-1
            i+=1
        return valor
    
    def Buscar (self, pat):
        bandera=0
        i=0
        while i <(len(self.__ListaMotos)):
            if pat == self.__ListaMotos[i].getPatente ():
                print ('Patente: ', self.__ListaMotos[i].getPatente())
                print ('Marca: ', self.__ListaMotos[i].getMarca())
                print ('Nombre y Apellido', self.__ListaMotos[i].getNyA())
                print ('Kilometrage', self.__ListaMotos[i].getKilometraje(), 'km')
                bandera=-1
            i+=1
        return bandera
    
    def Listar (self, p):
        for i in range (len(self.__ListaMotos)):
            print ('Patente: ', self.__ListaMotos[i].getPatente())
            print ('Nombre y Apellido: ', self.__ListaMotos[i].getNyA())
            acum=0
            for j in range (len(p._ManejadorPedido__ListaPedidos)):
                if self.__ListaMotos[i].getPatente()== p._ManejadorPedido__ListaPedidos[j].getPatenteasig():
                    print ('identificador de Pedido:', p._ManejadorPedido__ListaPedidos[j].getIdentificador())
                    print ('Cantidad de comidas:', p._ManejadorPedido__ListaPedidos[j].getComidas())
                    print ('Tiempo estimado de entrega:', p._ManejadorPedido__ListaPedidos[j].getTiempodeEntrega())
                    print ('Tiemporeal de entrega:', p._ManejadorPedido__ListaPedidos[j].getTiempoReal())
                    print ('Precio: ', p._ManejadorPedido__ListaPedidos[j].getPrecio())
                    acum+=float(p._ManejadorPedido__ListaPedidos[j].getPrecio())
            print ('Total recaudado: ', format(acum))
            print ('Comicion: ', format((acum*20)/100))

