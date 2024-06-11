import os
from modules.personas import Personas
from modules.ventas import Ventas
from modules.compras import Compras
from modules.stock import Stock

def menu_principal():
    '''Muestra el menú principal y retorna la opción seleccionada.'''
    print("\nMenú Principal:")
    print("1. Gestion Clientes/Proveedores.")
    print("2. Ventas.")
    print("3. Compras.")
    print("4. Gestion de Stock")
    print("5. Salir")

    opcion = int(input("Ingrese una opción: "))
    os.system("clear")
    return opcion

def gestion_clientes_y_proveedores():
  """Muestra las opciones de gestión de clientes y proceedores, y retorna la opción seleccionada."""
  print("\nGestión de Clientes y Proveedores:")
  print("1. Nuevo")
  print("2. Modificar")
  print("3. Borrar")
  print("4. Volver")

  opcion = int(input("Ingrese una opción: "))
  return opcion

def gestion_ventas():
  """Muestra las opciones de gestión las operaciones de venta y retorna la opción seleccionada."""
  print("\nGESTION de VENTAS:")
  print("1. Nueva venta")
  print("2. Consulta de Ventas")
  print("3. Devoluci�n de producto")
  print("4. Volver")

  opcion = int(input("Ingrese una opción: "))
  return opcion

def gestion_compras():
  """Muestra las opciones de gestión las operaciones de compra y retorna la opción seleccionada."""
  print("\nGESTION de COMPRAS:")
  print("1. Nueva compra")
  print("2. Consulta de compra")
  print("3. Devoluci�n de producto")
  print("4. Volver")

  opcion = int(input("Ingrese una opción: "))
  return opcion

def gestion_stock():
  """Muestra las opciones de para la gestion de los productos en stock; incluye:
  1) modificar el precio de los productos
  2) modificar la cantidad de producto en estok devido a operaciones no relacionadas 
  con la compra o la venta de los productos.
  3) Gestionar las categorias de los productos
  4) realizar consultas sobre los productos en stock
  ."""
  print("\nGESTION de PRODUCTOS EN STOCK:")
  print("1. Modificar precio producto")
  print("2. Ajuste de Stock de producto")
  print("4. Consulta por proveedor")
  print("5. Consulta por categoria")
  print("6. Agregar categoria")
  print("7. Modificar categoria")
  print("8. Borrar categoria")
  print("9. Volver")

  opcion = int(input("Ingrese una opción: "))
  return opcion

'''Ejecuta el menu'''
while True:
    opcion = menu_principal()
    if opcion == 1:
        opcion_gestion_clientes_y_proveedores = gestion_clientes_y_proveedores()
        print(opcion_gestion_clientes_y_proveedores)
        if opcion_gestion_clientes_y_proveedores == 1:
            Personas().registrar_persona()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_clientes_y_proveedores == 2:
            Personas().modificar_persona()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_clientes_y_proveedores == 3:
            Personas().eliminar_persona()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_clientes_y_proveedores == 4:
            os.system("clear")
            continue
        else:
            print("Opción inválida")
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
    elif opcion == 2:
        opcion_gestion_ventas =  gestion_ventas()
        if opcion_gestion_ventas == 1:
            Ventas().nueva_venta()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_ventas == 2:
            Ventas().consulta_ventas()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_ventas == 3:
            Ventas().devolucion()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_ventas == 4:
            os.system("clear")
            continue
        else:
            print("Opción inválida")
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
    elif opcion == 3:
        opcion_gestion_compras =  gestion_compras()
        if opcion_gestion_compras == 1:
            Compras().nueva_compra()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_compras == 2:
            Compras().consulta_compras()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_compras == 3:
            Compras().devolucion()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_compras == 4:
            os.system("clear")
            continue
        else:
            print("Opción inválida")
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
    elif opcion == 4:
        opcion_gestion_stock =  gestion_stock()
        if opcion_gestion_stock == 1:
            Stock().modificar_precio()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_stock == 2:
            Stock().modificar_cantidad()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_stock == 3:
            Stock().consulta_producto()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_stock == 4:
            Stock().consulta_proveedor()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_stock == 5:
            Stock().consulta_categoria()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_stock == 6:
            Stock().crear_categoria()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_stock == 7:
            Stock().modificar_categoria()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue
        elif opcion_gestion_stock == 8:
            Stock().eliminar_categoria()
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue       
        elif opcion_gestion_stock == 9:
            os.system("clear")
            continue
        else:
            print("Opción inválida")
            input("\nPresione ENTER para continuar")
            os.system("clear")
            continue               
    elif opcion == 5:
        break
    else:
        print("Opción inválida")
        input("\nPresione ENTER para continuar")
        os.system("clear")
