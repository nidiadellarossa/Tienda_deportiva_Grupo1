import datetime
from coneccionBD import GestionBD

class Compras():
    def __init__(self):
        self.proveedor = None
        self.productos = []
        self.tipo_pago = None
        self.productos = []
        self.dbmanager = GestionBD() 

    def nueva_compra(self):
        '''
        Este metodo tiene por objetivo registrar una nueva compra en la base de datos
        1) se ingresa el documento del proveedor, si no se encuentra en la base de datos se 
        da el error y se pide al usuario a registrar el proveedor
        2) si el proveedor existe se ingresan lo codigos de los productos y las cantidades
        3) cada vez que se ingresa un producto se verifica que existe  en la base de datos,
        si existe se agrega a la lista de las compras junto con la cantidad y se calcula el
        subtotal del producto y el total calculado.
        4) se confirma la compra  y se guardar los registros en la base de datos

        '''
        documento = input("Ingrese el documento del proveedor: ")
        
        fecha_compra = datetime.datetime.now().isoformat()

        registrar_producto = True
        total = 0
        lista_de_productos = []

        while registrar_producto:
            codigo = input("Ingrese el codigo del producto: ")
            precio =  float(input("Precio de venta: "))
            cantidad_comprada = float(input("cantidad ingresada: "))
            ''' 
            Aqui se verifica si el producto esta en la base de datos
            si está en la base de datos se procedera a ingresar la cantidad
            y el precio unitario de venta del producto (si hay modificacion).
            Si el codigo no se encuentra se procedera al registro del producto
            en la base de datos.
            '''
            mocked_producto = {
                "codigo": "12345678",
                "denominacion": "Topper Running T39",
                "precio": 1000,
                "stock": 1000
            }

            lista_de_productos.append({
                "codigo": mocked_producto["codigo"],
                "denominacion": mocked_producto["denominacion"],
                "precio": mocked_producto["precio"],
                "cantidad": cantidad_comprada,
            })
            registrar_producto_option = input("¿Desea registrar otro producto? (s/n): ")
            if registrar_producto_option == "n":
                registrar_producto = False

        confirmacion = input("Confirma la compra (s/n): ")
        if confirmacion == "s":
            '''
            Al confirmase la compra se registran los datos en las tablas operaciones 
            y en la tabla detalle operacion 
            '''
            print("Compra realizada correctamente")

    def consulta_compras(self):
        '''
        Este metodo tiene por objetivo consultar las compras realizadas en la base de datos
        Opciones de busqueda
        1)consulta de compras por producto
        2)consulta de compras por cliente
        3)Total de compras diarias por fecha
        '''

        menu_on = True
        while menu_on:
            print("1. Consulta de compras por producto")
            print("2. Consulta de compras por cliente")
            print("3. Total de compras diarias por fecha")
            print("4. Volver")

            opcion = int(input("Ingrese una opción: "))

            if opcion == 1:
                '''
                1) se ingresa el codigo del producto
                2) se verifica si el producto existe en la base de datos
                3) se obtienen los datos del producto
                4) se obtienen las compras realizadas por el producto
                5) se calcula el total de compras del producto
                6) se imprimen los datos de la consulta
                '''
                codigo = input("Ingrese el codigo del producto: ")
                fecha_inicio = input("Fecha Inicial: ")
                fecha_final = input("Fecha Final: ")

                '''
                si no se ingresan fechas se calcula el total de compras del producto
                si solo se ingresa la fecha inicial se calcula el total hasta el dia de hoy
                si solo se ingresa la fecha final se calcula el total desde la primer fecha hasta 
                la fecha final
                si se ingresan ambas fechas se calcula el total de compras del producto en el periodo
                '''
            if opcion == 2:
                '''
                1) se ingresa el documento del cliente
                2) se verifica si el cliente existe en la base de datos
                3) se obtienen los datos del cliente
                4) se obtienen las compras realizadas por el cliente
                5) se calcula el total de compras del cliente
                6) se imprimen los datos de la consulta
                '''
                documento = input("Ingrese el documento del cliente: ")
                fecha_inicio = input("Fecha Inicial: ")
                fecha_final = input("Fecha Final: ")
            
            if opcion == 3:

                '''
                1) se obtienen las compras realizadas en todas las categorias 
                en el periodo.
                2) se calcula el total de compras del periodo
                3) se imprimen los datos de la consulta
                '''
                fecha_inicio = input("Fecha Inicial: ")
                fecha_final = input("Fecha Final: ")
            if opcion == 4:
                break
            continuar = input("¿Desea realizar otra consulta?:")
            if continuar == "n":
                menu_on = False
            if opcion == 4:
                break
    
    def devolucion(self):
        '''
        Este metodo tiene por objetivo registrar una devolucion en la base de datos
        se ingresa el documento del proveedor, el codigo del producto y la cantidad
        se verifica que el producto exista en la base de datos
        se actualiza el stock del producto
        se registra la devolucion en la base de datos
        '''
        documento = input("Ingrese el documento del proveedor: ")
        codigo = input("Ingrese el codigo del producto: ")
        cantidad = input("Ingrese la cantidad de devolucion: ")

        confirmar = input("Confirmar la devolucion: ")
        if confirmar == "s":
            print("Devolucion realizada correctamente")


