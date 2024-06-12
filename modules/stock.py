from coneccionBD import GestionBD

class Stock():
    def __init__(self):
        self.codigo = None
        self.nombre = None
        self.precio = None
        self.cantidad = None
        self.categoria = None
        self.proveedor = None
        self.dbmanager = GestionBD() 

    def modificar_precio(self):
        '''
        Este método modifica el precio de venta de un producto ya registrado en la 
        base de datos independientemente de la cantidad del producto en cuestion en stock
        Se ingresa el codigo del producto. Si no se encuentra registrado se devuelve mensaje de
        error para volver a ingresar el codigo
        '''
        print("Modificar precio de producto")
        
        modificar_on = True
        while modificar_on:
            self.codigo = input("Ingrese el código del producto: ")
            '''
            Aqui se verifica si el producto se encuentra en la base de datos
            si se encuentra se imprime en pantalla el código del producto,
            la denominación del producto, y el precio de venta actual
            '''
            self.precio = input("Ingrese el nuevo precio: ")
            print(f"El precio del producto {self.codigo} se ha modificado a {self.precio}")
            confirmar = input("Confirmar nuevo precio (s/n): ")
            if confirmar == "s":
                'se modifica el precio para el producto en la base de datos'
                print("Precio modificado correctamente")
            consulta = input("Desea modificar el precio de otro producto (s/n): ")
            if consulta == "n":
                modificar_on = False
    
    def modificar_cantidad(self):
        '''
        Este método modifica la cantidad de un producto ya registrado en la 
        base de datos.
        Se ingresa el codigo del producto. Si no se encuentra registrado se devuelve mensaje de
        error para volver a ingresar el codigo
        '''
        print("Modificar el stock  de producto")
        
        modificar_on = True
        while modificar_on:
            self.codigo = input("Ingrese el código del producto: ")
            '''
            Aqui se verifica si el producto se encuentra en la base de datos
            si se encuentra se imprime en pantalla el código del producto,
            la denominación del producto, y la cantidad actual
            '''
            self.precio = input("Ingrese la nueva cantidad: ")
            print(f"La cantidad del producto {self.nombre} se ha modificado a {self.cantidad}")
            confirmar = input("Confirmar nuevo precio (s/n): ")
            if confirmar == "s":
                '''se modifica la cantidad para el producto en la base de datos'''
                print("Stock modificado correctamente")
            consulta = input("Desea modificar el stock de otro producto (s/n): ")
            if consulta == "n":
                modificar_on = False
    def consulta_producto(self):
        '''
        Este método consulta los datos de sobre un producto.
        Devuelve Denominacion, Categoria, Proveedor, Precio de Venta y
        Stock del producto.
        '''
        print("Consulta de Producto")
        
        modificar_on = True
        while modificar_on:
            self.codigo = input("Ingrese el código del producto: ")
            '''
            Aqui se verifica si el producto se encuentra en la base de datos
            si se encuentra se imprime en pantalla los datos del producti
            '''
            consulta = input("Desea consultar otro producto (s/n): ")
            if consulta == "n":
                modificar_on = False
    
    def consulta_proveedor(self):
        '''
        Este método de consulta devuelve los datos del proveedor
        y un listado de los productos en stock proveidos por el,
        que incluye categorias de producto, precio y cantidad de cada uno
        '''
        print("Consulta de Proveedor")
        
        modificar_on = True
        while modificar_on:
            self.proveedor = input("Ingrese el código del proveedor: ")
            '''
            Aqui se verifica si el proveedor se encuentra el la base de datos.
            si se encuentra se imprime en pantalla los datos del proveedor
            y los datos de los productos proveidos por el
            '''
            consulta = input("Desea consultar otro producto (s/n): ")
            if consulta == "n":
                modificar_on = False 
    def consulta_categoria(self):
        '''
        Este método de consulta devuelve un listado de productos que pertenencen a una
        categoria y los datos asociados a cada producto incluyendo denominacion, precio 
        y cantidad de cada uno
        '''
        print("Consulta de Categoria")
        
        modificar_on = True
        while modificar_on:
            self.categoria = input("Ingrese la Categoria: ")
            '''
            Aqui se verifica si la categoria se encuentra en la base de datos.
            si se encuentra se imprime en pantalla los datos de la categoria
            y los datos de los productos en stock de la categoria
            '''
            consulta = input("Desea consultar otro producto (s/n): ")
            if consulta == "n":
                modificar_on = False       

    def crear_categoria(self):
        '''
        Este método crea una nueva categoria 
        '''
        print("Crer Categoria")
        nueva_categoria = input("Ingrese nombre de categoria: ")

        confirmar = input("Confirmar nueva categoria(s/n): ")
        if confirmar == "s":
            print("Categoria creada correctamente")

        '''
        Aqui se guarda la nueva categoria en la base de datos.
        '''

    def modificar_categoria(self):
        '''
        Este método modifica una categoria existente
        '''
        print("Modificar Categoria")
        categoria = input("Ingrese nombre de categoria: ")

        '''
        Se busca la categoria en la base de datos. Si se encuentra se 
        devuelve el registro  de la base de datos.
        '''
        categoria = input("Ingrese nuevo nombre de la categoria: ")
        '''
        Aqui se reemplaza el nombre de la categoria para el id obtenido en la busqueda
        '''
        confirmar = input("Confirmar nueva categoria(s/n): ")
        if confirmar == "s":
            print("Categoria creada correctamente")
            '''
            Aqui se guarda la nueva categoria en la base de datos.
            '''
    def borrar_categoria(self):
        '''
        Este método borra una categoria existente
        '''
        print("Borrar Categoria")
        categoria = input("Ingrese nombre de categoria: ")

        '''
        Se busca la categoria en la base de datos. Si se encuentra se 
        devuelve el registro  de la base de datos.
        '''
        confirmar = input("Confirmar borrar categoria(s/n): ")
        if confirmar == "s":
            print("Categoria borrada correctamente")
            '''
            Aqui se borra la categoria en la base de datos.
            '''
