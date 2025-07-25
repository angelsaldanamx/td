from flask import Flask, request, session
from database.modelo import Modelo
import mysql.connector
from mysql.connector import Error
class Demanda():
    def __init__(self): 
        self.__comercializador=""
        self.__producto=""
        self.__fecha =""
    

    def registrar_demanda(self):
        try:
            self.__comercializador = session["id_usuario"]
            self.__producto = request.form["producto"]
            self.__fecha = request.form["fecha"]
            
            comandoSql = "INSERT INTO mkp(id_comercializador, producto, fecha_entrega) values(%s, %s, %s);"
            data = [self.__comercializador,self.__producto, self.__fecha]
            baseDeDatos = Modelo(comandoSql,data,1)
            baseDeDatos.comando()
        except Error as err:
            return print(f"No se pudo registar la demanda{err}")
        finally:
            pass
    def buscar_demanda(self):
        try:
            self.__comercializador = session["id_usuario"]
            self.__producto = request.form["producto"]
            self.__fecha = request.form["fecha "]
            
            comandoSql = "SELECT * FROM mkp WHERE producto LIKE %s AND fecha = %s;"
            data = [self.__producto, self.__fecha]
            baseDeDatos = Modelo(comandoSql,data,0)
            resultadosDB = baseDeDatos.comando()
        except :
            resultadosDB = None
        finally:
            return resultadosDB       
      
    def buscar_demandas_publicadas(self):
        try:
            self.__comercializador = session["id_usuario"]
            
            comandoSql = "SELECT * FROM mkp WHERE id_comercializador = %s;"
            data = [self.__comercializador]
            baseDeDatos = Modelo(comandoSql,data,0)
            resultadosDB = baseDeDatos.comando()
        except :
            resultadosDB = None
        finally:
            return resultadosDB  