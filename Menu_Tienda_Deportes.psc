
Proceso Menu_Tienda_Deportes
	Definir opcion como entero;
	Definir opcion_submenu Como Entero;	
	Definir menu_on como logico;
	Definir submenu_on como logico;
	menu_on = verdadero;
	Escribir "SISTEMA GESTION DE TIENDA DE DEPORTES";
	
	mientras menu_on = verdadero hacer
		Escribir "1. Gestion Clientes/Proveedores.";
		Escribir "2. Ventas.";
		Escribir "3. Compras.";
		Escribir "4. Gestion de Stock";
		Escribir "5. Salir";
		
		Escribir "Seleccione una opción:";
		Leer opcion;
		
		si opcion = 1 Entonces
			submenu_on = verdadero;
			mientras submenu_on Hacer
				Borrar Pantalla;
				Escribir  "GESTION de CLIENTES y PROVEEDORES";
				Escribir "1. Nuevo";
				Escribir "2. Modificar";
				Escribir "3. Borrar";
				Escribir "4. Volver";
				
				Escribir "Seleccione una opción:";
				leer opcion_submenu;
				
				si opcion_submenu = 1 Entonces
					Borrar Pantalla;
					Escribir "Esta opción crea un nuevo cliente/proveedor. El usuario debe ingresar los datos de la tabla personas, dirección, telefono, email. Para el caso de personas físicas (cuyo tipo de documento es DNI) se puede registrar de manera opcional la fecha de nacimiento y género.";
					Escribir "Presione cualquier tecla para continuar";
					Esperar tecla;
				FinSi
				si opcion_submenu = 2 Entonces
					Borrar Pantalla;
					Escribir "Esta opción modifica los datos de un cliente/proveedor ya registrado. Es necesario ingresar el documento de la persona física o jurídica para acceder a sus datos y modificarlos";
					Escribir "Presione cualquier tecla para continuar";
					Esperar Tecla;
				FinSi
				si opcion_submenu = 3 Entonces
					Borrar Pantalla;
					Escribir  "Esta opción permite borrar un cliente/proveedor ya registrado. Es necesario ingresar el documento de la persona física o jurídica para borrarlo";
					Escribir "Presione cualquier tecla para continuar";
					Esperar Tecla;
				FinSi
				si opcion_submenu = 4 Entonces
					Borrar Pantalla;
					submenu_on = falso;
				FinSi
			FinMientras
		FinSi
		si opcion = 2 Entonces
			submenu_on = verdadero;
			mientras submenu_on Hacer
				Escribir  "GESTION de VENTAS";
				Escribir "1. Nueva venta";
				Escribir "2. Consulta de Ventas";
				Escribir "3. Devolución de producto";
				Escribir "4. Volver";
				
				Escribir "Seleccione una opción:";
				leer opcion_submenu;
				
				si opcion_submenu = 1 Entonces
					Borrar Pantalla;
					Escribir "Esta opción registra una nueva venta. En la tabla de operaciones crea la operacion de venta y en la tabla de detalle de operaciones  se registan los productos, precios y cantidades vendidas. Se deduce la cantidad de cada producto del stock";
					Escribir "Presione cualquier tecla para continuar";
					Esperar Tecla;	
				FinSi
				si opcion_submenu = 2 Entonces
					Borrar Pantalla;
					Escribir "Esta opción hace consultas sobre las ventas realizadas";
					Escribir "Presione cualquier tecla para continuar";
					Esperar Tecla;
				FinSi
				si opcion_submenu = 3 Entonces
					Borrar Pantalla;
					Escribir "Esta opción permite registrar la devolución de un producto vendido, volviendo a registrar el ingreso del producto al stock";
					Escribir "Presione cualquier tecla para continuar";
					Esperar Tecla;
				FinSi
				si opcion_submenu = 4 Entonces
					Borrar Pantalla;
					submenu_on = falso;
				FinSi
			FinMientras
		FinSi
		si opcion = 3 Entonces
			submenu_on = verdadero;
			mientras submenu_on Hacer
				Escribir  "GESTION de COMPRAS";
				Escribir "1. Nueva compra";
				Escribir "2. Consulta de compras";
				Escribir "3. Devolución de producto";
				Escribir "4. Volver";
				
				Escribir "Seleccione una opción:";
				leer opcion_submenu;
				
				si opcion_submenu = 1 Entonces
					Borrar Pantalla;
					Escribir "Esta opción registra una nueva compra. En la tabla de operaciones crea la operacion de compra y en la tabla de detalle de operaciones  se registan los productos, precios y cantidades compradas. Se agrega la cantidad de cada producto del stock";
					Escribir "Presione cualquier tecla para continuar";
					Esperar Tecla;	
				FinSi
				si opcion_submenu = 2 Entonces
					Borrar Pantalla;
					Escribir "Esta opción hace consultas sobre las compras realizadas";
					Escribir "Presione cualquier tecla para continuar";
					Esperar Tecla;
				FinSi
				si opcion_submenu = 3 Entonces
					Borrar Pantalla;
					Escribir "Esta opción permite registrar la devolución de un producto comprado, registrando la salida del producto al stock";
					Escribir "Presione cualquier tecla para continuar";
					Esperar Tecla;
				FinSi
				si opcion_submenu = 4 Entonces
					Borrar Pantalla;
					submenu_on = falso;
				FinSi
			FinMientras
		FinSi
		si opcion = 4 Entonces
			submenu_on = verdadero;
			mientras submenu_on Hacer
				Escribir  "GESTION de STOCk";
				Escribir "1. Modificar precio producto";
				Escribir "2. Ajuste de Stock de producto";
				Escribir "3. Consulta por producto";
				Escribir "4. Consulta por proveedor";
				Escribir "5. Consulta por categoria";
				Escribir "6. Agregar/Modificar categoria";
				Escribir "7. Salir";
				
				Escribir "Seleccione una opción:";
				leer opcion_submenu;
				
				si opcion_submenu = 1 Entonces
					Borrar Pantalla;
					Escribir "Esta opción  permite modificar el precio unitario de un producto";
					Escribir "Presione cualquier tecla para continuar";
					Esperar Tecla;
				FinSi
				si opcion_submenu = 2 Entonces
					Borrar Pantalla;
					Escribir "Esta opción permite hacer ajustes manuales en el stock de un producto";
					Escribir "Presione cualquier tecla para continuar";
					Esperar Tecla;
				FinSi
				si opcion_submenu = 3 Entonces
					Borrar Pantalla;
					Escribir "Esta opción permite consultar los datos guardados sobre un producto";
					Escribir "Presione cualquier tecla para continuar";
					Esperar Tecla;
				FinSi
				si opcion_submenu = 4 Entonces
					Borrar Pantalla;
					Escribir "Esta opción permite consultar los datos guardados sobre un producto";
					Escribir "Presione cualquier tecla para continuar";
					Esperar Tecla;
				FinSi
				si opcion_submenu = 5 Entonces
					Borrar Pantalla;
					Escribir "Esta opción permite consultar los datos relacionados a otros los productos relacionados con un proveedor";
					Escribir "Presione cualquier tecla para continuar";
					Esperar Tecla;
				FinSi
				si opcion_submenu = 6 Entonces
					Borrar Pantalla;
					Escribir "Esta opción permite consultar los datos relacionados a otros los productos relacionados con una categoria";
					Escribir "Presione cualquier tecla para continuar";
					Esperar Tecla;
				FinSi
				si opcion_submenu = 7 Entonces
					Borrar Pantalla;
					submenu_on = falso;
				FinSi
			FinMientras
		FinSi
		si opcion = 5 Entonces
			menu_on = Falso;
		FinSi
	FinMientras
	
FinProceso
