import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.cliente_model import Cliente
from fastapi.encoders import jsonable_encoder

class ClienteController:
        
    def create_cliente(self, cliente: Cliente):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO clientes (nombre,apellido,idtipodoc,documento,direccion,correo) VALUES (%s, %s, %s, %s, %s ,%s)", (cliente.nombre, cliente.apellido, cliente.idtipodoc, cliente.documento, cliente.direccion, cliente.correo))
            conn.commit()
            conn.close()
            return {"resultado": "Cliente creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_cliente(self, cliente_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes WHERE id = %s", (cliente_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'nombre':result[1],
                    'apellido':result[2],
                    'idtipodoc':int(result[3]),
                    'documento':result[4],
                    'direccion':result[5],
                    'correo':result[6]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                ##Esto interrumpe la ejecución y responde al cliente con un código 404
                ## comunica al cliente de la API qué pasó (error HTTP).
                ##código 404,comportamiento correcto según las reglas HTTP
                raise HTTPException(status_code=404, detail="Cliente not found")  
                
        except psycopg2.Error as err:
            print(err)
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            ##Maneja el estado de la transacción en la base de datos.Si un INSERT, UPDATE o DELETE falla dentro de una transacción, rollback() revierte esos cambios.
            conn.rollback()
        finally:
            conn.close()
       
    def get_clientes(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'nombre':data[1],
                    'idtipodoc':data[2],
                    'documento':data[3],
                    'direccion':data[4],
                    'correo':data[5]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Cliente not found")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    
    
       

##cliente_controller = ClienteController()