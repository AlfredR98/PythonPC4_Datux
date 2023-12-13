'''
Ejercicio 1
'''
'''
ruta_archivo = './scripts/software.txt'
with open(ruta_archivo, mode = 'r+', encoding='utf-8') as file:
    data = file.read().lower()
    repetir = data.count(' la')

    try:
        texto_adicional = input('Ingrese el texto adicional:\n')
    except Exception as e:
        print(e)

    dataw = file.write('\n'+texto_adicional)
    file.close()

print(f'\nLa palabra "la" se repite: \t{repetir} veces')
'''
'''
Ejercicio 2
'''
import modulos.bd as bd
import random
from modulos.proceso import *
from modulos.jobs import *
from modulos.cliente import *
from pyfiglet import Figlet
figlet = Figlet()

database=None
def main():
    salir=False
    init=True
    while not salir:
        #flag para que se inice solo una vez
        if init:
            user=input("ingrese su nombre de usuario temporal: ") 
            init=False
            config() ## ejecutar las consideraciones basicas al iniciar la aplicacion
            fuentes = Figlet().getFonts()
            fAleatoria = random.choice(fuentes)
            figlet = Figlet(font=fAleatoria)
            textoRandom = 'Hello, world'
            ascii = figlet.renderText(textoRandom)
            print(ascii)
            
        opciones="""
        Bienvenidos a store DatuxTec
        1. Crear producto
        2. Listar productos
        3. Editar nombre de producto 
        4. Eliminar producto
        5. Mostrar Tipo Cambio SUNAT
        6. Editar precio producto
        7. Editar stock
        8. Agregar cliente
        9. Listar cliente
        10. Buscar producto
        11. Salir"""
        print(opciones)
        opc=int(input("ingrese una opcion: "))
        if opc==1:
            crear_producto(user)
        elif opc==2:
            listar_producto(user)
        elif opc==3:
            editar_nombre(user)
        elif opc==4:
            eliminar_producto(user)
        elif opc ==5:
            mostrar_dataSunat(user)
        elif opc ==6:
            editar_precio_producto(user)
        elif opc ==7:
            editar_stock(user)
        elif opc ==8:
          crear_cliente(user)
        elif opc ==9:
          listar_cliente(user)  
        elif opc ==10:
          buscar_producto(user)
        elif opc==11:
            salir=True
            print("terminando sesion....")
            break
        
        else:
            print("ingrese una opcion valida")

#funcion que configura la inicializacion de la aplicacion
def config():
    database=bd.Bd()
    query_products="""
        CREATE TABLE  IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    price REAL NOT NULL,
                    stock INTEGER NOT NULL
                );
    """
    database.execute_query(query_products)

    query_tipoCambio="""
        CREATE TABLE  IF NOT EXISTS tipoCambio (
                    id INTEGER PRIMARY KEY,
                    compra DOUBLE NOT NULL,
                    venta DOUBLE NOT NULL,
                    origen VARCHAR(5) NOT NULL,
                    moneda char(3) NOT NULL,
                    fecha datetime NOT NULL
                );
    """
    database.execute_query(query_tipoCambio)

    query_cliente="""
        CREATE TABLE  IF NOT EXISTS cliente (
                    id_cliente INTEGER PRIMARY KEY,
                    nombres VARCHAR(50) NOT NULL,
                    apellidos VARCHAR(50) NOT NULL,
                    celular char(9) NOT NULL,
                    correo varcahr(20) NOT NULL
                );
    """
    database.execute_query(query_cliente)

if __name__=='__main__':
    main()