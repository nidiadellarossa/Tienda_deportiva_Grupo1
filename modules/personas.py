from coneccionBD import GestionBD
class Personas():
    def __init__(self):
        self.documento = None
        self.tipo_documento = None
        self.razon_social = None
        self.calle = None
        self.numero = None
        self.piso = None
        self.departamento = None
        self.localidad = None
        self.codigo_postal = None
        self.provincia = None
        self.email = []
        self.telefono = []
        self.fecha_nacimiento = None
        self.genero = None
        self.tabla_campos = {
            "documento": "Documento",
            "tipo_documento": "Tipo de documento",
            "razon_social": "Razón social",
            "calle": "Calle",
            "numero": "Número",
            "piso": "Piso",
            "departamento": "Departamento",
            "localidad": "Localidad",
            "codigo_postal": "Código postal",
            "provincia": "Provincia",
            "email": "Email",
            "telefono": "Teléfono",
            "fecha_nacimiento": "Fecha de nacimiento",
            "genero": "Género"
        }
        self.dbmanager = GestionBD() 
        
    def registrar_persona(self):
        '''Metodo para registrar los datos de un nuevo cliente / proveedor'''

        self.documento = input("Ingrese el documento: ")
        self.tipo_documento = input("Ingrese el tipo de documento: ")
        self.razon_social = input("Ingrese la razón social: ")
        self.calle = input("Ingrese la calle: ")
        self.numero = input("Ingrese el número: ")
        self.piso = input("Ingrese el piso: ")
        self.departamento = input("Ingrese el departamento: ")
        self.localidad = input("Ingrese la localidad: ")
        self.codigo_postal = input("Ingrese el código postal: ")
        self.provincia = input("Ingrese la provincia: ")
        
        email_input = True
        while email_input:
            email_adress = input("Ingrese el email: ")
            self.email.append(email_adress)
            email_input = input("¿Desea ingresar otro email? (s/n): ")
            if email_input == "n":
                email_input = False

        telefono_input = True
        while telefono_input:
            telefono_numero = input("Ingrese el teléfono: ")
            self.telefono.append(telefono_numero)
            telefono_input = input("¿Desea ingresar otro teléfono? (s/n): ")
            if telefono_input == "n":
                telefono_input = False

        is_persona_fisica = input("Es una persona fisica (s/n); ")
        if is_persona_fisica == "s":
            self.fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")
            self.genero = input("Ingrese el género: ")

        print("CONFIRMAR DATOS")
        print("Documento: ", self.documento)
        print("Tipo de documento: ", self.tipo_documento)
        print("Razón social: ", self.razon_social)
        print("Calle: ", self.calle)
        print("Número: ", self.numero)
        print("Piso: ", self.piso)
        print("Departamento: ", self.departamento)
        print("Localidad: ", self.localidad)
        print("Código postal: ", self.codigo_postal)
        print("Provincia: ", self.provincia)
        print("Email: ")
        for email in self.email:
            print(email)
        print("Teléfono: ")
        
        for telefono in self.telefono:
            print(telefono)
        
        if is_persona_fisica == "s":
            print("Fecha de nacimiento: ", self.fecha_nacimiento)
            print("Género: ", self.genero)

        """Se pide confirmacio para guardar los datos en base de datos"""
        confirmacion = input("Confirma los datos (s/n): ")
        if confirmacion == "s":
            self.dbmanager.connect()
            query_persona = """
            INSERT INTO tienda_ropa.persona (documento, tipo_documento, razon_social) 
            VALUES (%s, %s, %s)
            """
            self.dbmanager.execute_query(query_persona, (self.documento, self.tipo_documento, self.razon_social))
            
            query_direccion_fiscal = """
            INSERT INTO tienda_ropa.direccion_fiscal (id_persona, calle, numero, piso, departamento, id_localidad) 
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.dbmanager.execute_query(query_direccion_fiscal, (self.documento, self.calle, self.numero, self.piso, self.departamento, self.codigo_postal))

            query_email = """
            INSERT INTO tienda_ropa.email (id_persona, direccion) 
            VALUES (%s, %s)
            """

            for email in self.email:
                self.dbmanager.execute_query(query_email, (self.documento, email))

            query_telefono = """
            INSERT INTO tienda_ropa.telefono (id_persona, numero) 
            VALUES (%s, %s)
            """

            for telefono in self.telefono:
                self.dbmanager.execute_query(query_telefono, (self.documento, telefono))
            
            if is_persona_fisica == "s":
                query_persona_fisica = """
                INSERT INTO tienda_ropa.persona_fisica (id_persona, fecha_nacimiento, genero) 
                VALUES (%s, %s, %s)
                """
                self.dbmanager.execute_query(query_persona_fisica, (self.documento, self.fecha_nacimiento, self.genero))

            self.dbmanager.disconnect()
            print("Datos ingresados correctamente")            
        else:
            print("Datos no ingresados")

    def modificar_persona(self):
        '''Metodo para modificar los datos de un cliente / proveedor
        1) Consulta a la base de datos los datos del cliente a modificar. Se pueden modificar
        todos los datos excepto el número de documento y el tipo de documento
        2) Se muestras los datos actuales del cliente y luego un menu para elegir el dato a modificar
        3) se muestra el campo del dato a modificar 
        4) se pide confirmacion del dato a modificar y se pregunta si se desea modidicar otro dato 
        5) se graban todos los datos modificados  
        '''
        documento_buscado = input('Ingrese el numero de documento a buscar: ') #Se accedera a esta variable cuando se haga la búsqueda

        '''
        A continuacion se deberia realizar la consulta a la base de datos para obtener los datos
        asociados al documentro ingresado. Sin no encuentra el documento en la base de datos se debe mostrar 
        mensaje de error. La busqueda de los datos se debe realizar dentro de un bloguqe try/catch
        La variable Mocked_data a constinuacion se tiene los datos mokeados de una respuesta de base de datos 
        '''

        mocked_data = {
            "documento": "12345678",
            "tipo_documento": "DNI",
            "razon_social": "Empresa de prueba",
            "calle": "Calle de prueba",
            "numero": "123",
            "piso": "1",
            "departamento": "A",
            "localidad": "Localidad de prueba",
            "codigo_postal": "1234",
            "provincia": "Provincia de prueba",
            "email": ["email1", "email2"],
            "telefono": ["123456789", "987654321"],
            "fecha_nacimiento": "2000-01-01",
            "genero": "Masculino"
        }

        modificar_datos = True
    
        while modificar_datos:
            '''A continuacion se muestran en pantalla los datos del cliente
            se muestra el numero de opcion para seleccionar cual dato modificar 
            '''
            numero_opcion = 0
            opciones = []

            for key in mocked_data:  
                numero_opcion += 1
                val = mocked_data[key] 
                opciones.append(key)
                print(f"{numero_opcion} - {self.tabla_campos[key]}: {val}")

            '''
            A continuacion se selecciona la opcion a modificar
            Al terminar se consulta si se quiere seleccionar otro dato para modificar
            '''

            print("Seleccione el dato a modificar: ")
            opcion_seleccionada = int(input())

            if opcion_seleccionada > len(opciones):
                print("Opcion no valida")
            else:
                if opciones[opcion_seleccionada - 1] in ['email', 'telefono']:
                    orden_item = 0
                    for item in mocked_data[opciones[opcion_seleccionada - 1]]:
                        orden_item += 1
                        print(f'{orden_item} - modificar {item}')
                    orden_item += 1
                    print (f'{orden_item} - agregar {self.tabla_campos[opciones[opcion_seleccionada - 1]]}')
                    opcion_item = int(input())

                    if opcion_item > len(opciones[opcion_seleccionada - 1]) + 1:
                        print("Opcion no valida")
                    else:
                        nuevo_valor_opcion = input(f'Ingrese el nuevo valor para {self.tabla_campos[opciones[opcion_seleccionada - 1]]}: ')
                        print(f'El nuevo valor para {self.tabla_campos[opciones[opcion_seleccionada - 1]]} es: {nuevo_valor_opcion}')

                        nuevo_valor = mocked_data[opciones[opcion_seleccionada - 1]]
                        if opcion_item > len(nuevo_valor):
                            nuevo_valor.append(nuevo_valor_opcion)
                        else:
                            nuevo_valor[opcion_item-1] = nuevo_valor_opcion

                else:
                    nuevo_valor = input(f'Ingrese el nuevo valor para {self.tabla_campos[opciones[opcion_seleccionada - 1]]}: ')
                    print(f'El nuevo valor para {self.tabla_campos[opciones[opcion_seleccionada - 1]]} es: {nuevo_valor}')
                        

                confirmacion = input("Confirma los datos (s/n): ")
                if confirmacion == "s":
                    mocked_data[opciones[opcion_seleccionada - 1]] = nuevo_valor
                    print("Datos ingresados correctamente")
                modificar_datos = input("¿Desea modificar otro dato? (s/n): ")
                if modificar_datos == "n":
                    modificar_datos = False

    def eliminar_persona(self):
        '''
        Este método tiene por objeto eliminar un cliente / proveedor de la base de datos
        1) Se ingresa el documento del cliente / proveedor 
        2) se verifica que el documento exista en la base de datos y si existe se muestra el documento y la razon social el pantalla
        3) se verifica con el usuario si se procede a borrar el registro
        4) se confirma el resultado
        '''

        documento_buscado = input('Ingrese el numero de documento a buscar: ') #Se accedera a esta variable cuando se haga la búsqueda

        '''
        A continuacion se deberia realizar la consulta a la base de datos para obtener los datos
        asociados al documentro ingresado. Sin no encuentra el documento en la base de datos se debe mostrar 
        mensaje de error. La busqueda de los datos se debe realizar dentro de un bloque try/catch
        La variable Mocked_data a continuacion se tiene los datos mokeados de una respuesta de base de datos 
        '''

        mocked_data = {
            "documento": "12345678",
            "tipo_documento": "DNI",
            "razon_social": "Empresa de prueba",
        }

        '''
        Aqui se muestra el documento y la razon social del cliente seleccionado
        '''
        print(f"Cliente/Proveedor a eliminar: {mocked_data['razon_social']}, {mocked_data['tipo_documento']} {mocked_data['documento']} .")

        confirmacion = input("¿Confirma eliminar cliente / proveedor? (s/n): ")

        if confirmacion == "s":
            print("Datos eliminados correctamente")
    
