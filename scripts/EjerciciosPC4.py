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
from modulos.proceso import *

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
        opciones="""
        Bienvenidos a store DatuxTec
        1. Crear producto
        2. Listar productos
        3. Editar nombre de producto 
        4. Eliminar producto
        5. Salir"""
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
        elif opc==5:
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


if __name__=='__main__':
    main()
    