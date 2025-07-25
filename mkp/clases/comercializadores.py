from flask import request
from database.modelo import Modelo
import mysql.connector
class Comercializadores():
    def __init__(self):
        self.__usuario = ""
        self.__password = ""
       
    def autenticacion(self):
        try:
        # Obtener datos del formulario
            self.__usuario = request.form['usuario']
            self.__password = request.form['password']

            # Preparar datos para la Base de Datos
            data = [
                self.__usuario,
                self.__password
            ]
            comandoSql = "SELECT id_comercializador, usuario, pssword FROM comercializadores WHERE usuario = %s and pssword = %s" 
            baseDeDatos = Modelo(comandoSql, data, 0)
            resultadoBD = baseDeDatos.comando()
        except:
            resultadoBD = None
        finally:
            return resultadoBD

    def registrar_comercializador(self):
        # Obtener datos del formulario
            self.__nombre = request.form['nombre']
            self.__apellidoP = request.form['apellidoP']
            self.__apellidoM = request.form['apellidoM']
            self.__direccion ={
                'direccion' : {
                    'calle' : request.form['calle'],
                    'ciudad' : request.form['ciudad'],
                    'estado' : request.form['estado'],
                    'pais' : request.form['pais']
                },
                'contacto' : {
                    'email' : request.form['email'],
                    'telefono' : request.form['telefono']
                }
            }
            self.__usuario = request.form['usuario']
            self.__password = request.form['password']
            
            #Conexion
            try:
                datos = [self.__nombre, self.__apellidoP, self.__apellidoM, self.__direccion, self.__usuario, self.__password]
                comandoSql = "INSERT INTO comercializadores (nombre, apellidoP, apellidoM, direccion, usuario, pssword) VALUES (%s, %s,%s,%s, %s,%s)"                
                baseDeDatos = Modelo(comandoSql, datos, 1)
                baseDeDatos.comando()
                
            except ErrorSQL as err:
                return f"No se pudo insertar los datos {err}"
            finally:
                pass 