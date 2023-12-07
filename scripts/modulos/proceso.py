from modulos.bd import * 
from modulos.log import *
## el programa se ejecuta desde main por eso importas como si estuvieras desde main

logger=Log() # INSTANCIAMOS LOG
BdIv2=Bd() # podemos crear una instancia global
class Product:
    def __init__(self,name,price,stock) -> None:
        self.name=name
        self.price=price
        self.stock=stock
    def tuplaDatos(self):
        #retorno una tupla por que sqlite para insertar se necesita una tupla
        return (self.name,self.price,self.stock) 

def crear_producto(user):
    BdI=Bd() 
    print("ingrese informacion del producto")
    name=input("ingrese el valor para nombre: ")
    price=float(input("ingrese el valor para precio: "))
    stock=int(input("ingrese el valor para stock: "))
    p1=Product(name,price,stock)
    try:
        query=f"insert into products(name,price,stock) values('{p1.name}','{p1.price}','{p1.stock}')"
        BdI.execute_query(query)
        loogeinfo=f"-{user}-creo un producto-{p1.name} ,{p1.price},{p1.stock} "
        logger.register_log(loogeinfo)
    except Exception as e:
        loogeinfo=f"-{user}-error al crear un prodcuto-{e}  "
        logger.register_log(loogeinfo)


def listar_producto(user):
    print("Lista de productos")
    print('id|nombre|price|stock')
    query="select * from products"
    try:
        data=BdIv2.get_data(query)
        loogeinfo=f"-{user}-listo los products"
        logger.register_log(loogeinfo)
        for i in data:
            print(i[0],i[1],i[2],i[3])
    except Exception as e:
        loogeinfo=f"-{user}-error al listar los prodcuto-{e}  "
        logger.register_log(loogeinfo)
    
def eliminar_producto(user):
    id=int(input("ingrese el id del producto a elimninar"))
    query=f"DELET FROM products where id={id}"
    try:
        BdIv2.execute_query(query)
        loogeinfo=f"-{user}-se elimino un producto con id{id}"
        logger.register_log(loogeinfo)
    except Exception as e:
        loogeinfo=f"-{user}-error al ELIMINAR EL PRODUCTO -{e}  "
        logger.register_log(loogeinfo)

def editar_nombre(user):
    print("actualizar el nombre ")
    id=input("ingrese el id del producto a actualizar")
    nuevo_name=input("ingrese el nuevo nombre")
    query = f'''
        UPDATE products
        SET name = '{nuevo_name}'
        WHERE id = {id};
    '''
    try:
        BdIv2.execute_query(query)
        loogeinfo=f"-{user}-se actualizao un producto con id{id}"
        logger.register_log(loogeinfo)
    except Exception as e:
        loogeinfo=f"-{user}-error al actualizar EL PRODUCTO -{e}  "
        logger.register_log(loogeinfo)



## en caso queremos hacer una busqeuda al final del select * from tabla se agrega 
## la palabra where 