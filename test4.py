from GestorM import ManejadorMotos
from GestorP import ManejadorPedido

class test:
    m= ManejadorMotos()
    p= ManejadorPedido()
    m.CargarMotos()
    p.CargarPedidos()

    print ('1 _ Cargar nuevos pedidos')
    print ('2 _ Modificar tiempo real del pedido')
    print ('3 _ Calcular timepo promedio de un conductor')
    print ('4 _ Lista de conductor con su comision')
    print ('5 _ Ordenas los pedidos por patentes')
    print ('6 _ Mostrar arreglo')
    print ('0 _ Para salir del menu')

    op= int (input ('Ingrese la opcion: '))

    while op != 0:
        if op == 1:
            patente= input ('Ingrese la patente:')
            if m.Validar_Patente (patente)==-1:
                idpedido= input ('Ingrese el identificador de pedido:')
                comida= input ('Ingrese la cantidad de comida:')
                tiempoe= input ('Ingrese el tiempo de entrega:')
                tiemporeal=0
                precio= input ('Ingrese el precio:')
                Pedido_Nuevo= [patente, idpedido, comida, tiempoe, tiemporeal, precio]
                p.NuevoPedido(Pedido_Nuevo)
            else:
                print ('La patente ingresada es invalida')

        elif op==2:
            id= int (input('Ingrese el identificador de pedido: '))
            if p.Modificar_TiempoReal (id)==True:
                print ('El tiepo real se modifico correctamente')
        
        elif op==3:
            patente= input('Ingrese la patente de la moto que desea buscar: ')
            if m.Buscar (patente)==-1:
                p.Promedio (patente)
            else: print ('Patente no encontrada')
        
        elif op==4:
            m.Listar (p)
        
        elif op==5:
            p.Ordenar()

        
            
            
        elif op==6:
            p.Mostrar()
        op= int (input ('Ingrese la opcion: '))