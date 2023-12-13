import requests
from lxml import *
from modulos.bd import *
from modulos.log import *

Bdjob=Bd()
logger=Log()
url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
data=requests.get(url)

class jobs:

    def __init__(self,data):
        self.DataJson = data.json()
    
    def mostrarData(self):
        self.com = self.DataJson['compra'] 
        self.ven = self.DataJson['venta'] 
        self.ori = self.DataJson['origen'] 
        self.mon = self.DataJson['moneda'] 
        self.fec = self.DataJson['fecha'] 
    
    def insertar_dataSunat(self):
        try:
            query = f"insert into tipoCambio(compra,venta,origen,moneda,fecha) values ({self.com},{self.ven},'{self.ori}','{self.mon}','{self.fec}')"
            Bdjob.execute_query(query)
            print('Datos insertados de tipo cambio correctamente!')
            loogeinfo=f"-se insertó los datos del API Sunat- {self.com},{self.ven},{self.ori},{self.mon},{self.fec} "
            logger.register_log(loogeinfo)
        except Exception as e:
            loogeinfo=f"-error al listar los prodcuto-{e}  "
            logger.register_log(loogeinfo)

def mostrar_dataSunat(user):
        print("Listar datos tipo cambio")
        print('id|compra|venta|origen|moneda|fecha')
        query="select * from tipoCambio"
        try:
            data=Bdjob.get_data(query)
            loogeinfo=f"-{user}-listo los datos SUNAT"
            for i in data:
                print(i[0],i[1],i[2],i[3],i[4],i[5])
            logger.register_log(loogeinfo)
        except Exception as e:
            loogeinfo=f"-{user}-error al listar los prodcuto-{e}  "
            logger.register_log(loogeinfo)
     
j = jobs(data)
j.mostrarData()
j.insertar_dataSunat()



