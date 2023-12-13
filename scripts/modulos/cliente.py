from modulos.bd import * 
from modulos.log import *
## el programa se ejecuta desde main por eso importas como si estuvieras desde main

logger=Log() # INSTANCIAMOS LOG
BdIv3=Bd() # podemos crear una instancia global


class Cliente:
    def __init__(self,nom,ape,cel,correo):
        self.nom = nom
        self.ape = ape
        self.cel = cel
        self.correo = correo
    
    def tuplaDatos(self):
        #retorno una tupla por que sqlite para insertar se necesita una tupla
        return (self.nom,self.ape,self.cel,self.correo) 

def crear_cliente(user):
    BdI=Bd() 
    print("ingrese informacion del cliente")
    nom=input("ingrese sus nombres: ")
    ape=input("ingrese sus apellidos: ")
    cel=input("ingrese su número de celular: ")
    correo=input("ingrese su correo: ")
    c=Cliente(nom,ape,cel,correo)
    try:
        query=f"insert into cliente(nombres,apellidos,celular,correo) values('{c.nom}','{c.ape}','{c.cel}','{c.correo}')"
        BdI.execute_query(query)
        loogeinfo=f"-{user}-crear cliente-{c.nom},{c.ape},{c.cel},{c.correo}"
        logger.register_log(loogeinfo)
    except Exception as e:
        loogeinfo=f"-{user}-error al crear cliente-{e}  "
        logger.register_log(loogeinfo)

def listar_cliente(user):
    print("Lista de clientes")
    print('id|nombres|apellidos|celular|correo')
    query="select * from cliente"
    try:
        data=BdIv3.get_data(query)
        loogeinfo=f"-{user}-listo los clientes"
        for i in data:
            print(i[0],i[1],i[2],i[3],i[4])
    except Exception as e:
        loogeinfo=f"-{user}-error al listar los clientes-{e}  "
        logger.register_log(loogeinfo)