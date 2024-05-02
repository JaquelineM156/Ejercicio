import os
from Pedidos import Clase_Pedido
import csv

class ManejadorPedido:
    def __init__ (self):
        self.__ListaPedidos= []
    
    def CargarPedidos (self):
        archivo=open('Pedidos.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            p= Clase_Pedido(fila[0], int(fila[1]), int(fila[2]), int(fila[3]), float(fila[4]), float(fila[5]))
            self.__ListaPedidos.append(p)
        archivo.close()

    def Mostrar (self):
        for i in range (len(self.__ListaPedidos)):
            print ('Patente Asignada:', self.__ListaPedidos[i].getPatenteasig())
            print ('identificador de Pedido:', self.__ListaPedidos[i].getIdentificador())
            print ('Cantidad de comidas:', self.__ListaPedidos[i].getComidas())
            print ('Tiempo estimado de entrega:', self.__ListaPedidos[i].getTiempodeEntrega())
            print ('Tiemporeal de entrega:', self.__ListaPedidos[i].getTiempoReal())

    def NuevoPedido (self,nuevo):
        self.__ListaPedidos.append(nuevo)
    
    def Modificar_TiempoReal (self, ident):
        resultado=False
        i=0
        while i<(len(self.__ListaPedidos)):
            if self.__ListaPedidos[i].getIdentificador () == ident:
                pat= input ('Ingrese la patente de la moto: ')
                if self.__ListaPedidos[i]. getPatenteasig ()==pat:
                    Tiempo= input ('Ingrese el nuevo tiempo real: ')
                    self.__ListaPedidos[i].ModificarT(Tiempo)
                    resultado=True
                else: print ('La patente igresada es incorrecta')
            i+=1
        return resultado
    
    def Promedio (self, pat):
        cont=0
        acum=0
        for i in range (len(self.__ListaPedidos)):
            if pat == self.__ListaPedidos[i].getPatenteasig():
                cont+=1
                acum+= int(self.__ListaPedidos[i].getTiempoReal())
        if acum ==0:
            print('El conductor', format(pat), 'No ah realizado pedidos')
        else: print ('El promedio de tiempo real es', format(acum/cont))

    def Ordenar (self):
        self.__ListaPedidos= sorted(self.__ListaPedidos)
        print ('-----------------------------------------Lista de Pedidos Ordenados---------------------------------------')
        for i in range (len(self.__ListaPedidos)):
            print ('Patente Asignada:', self.__ListaPedidos[i].getPatenteasig())
            print ('identificador de Pedido:', self.__ListaPedidos[i].getIdentificador())
            print ('Cantidad de comidas:', self.__ListaPedidos[i].getComidas())
            print ('Tiempo estimado de entrega:', self.__ListaPedidos[i].getTiempodeEntrega())
            print ('Tiemporeal de entrega:', self.__ListaPedidos[i].getTiempoReal())
            print ('Precio: ', self.__ListaPedidos[i].getPrecio())