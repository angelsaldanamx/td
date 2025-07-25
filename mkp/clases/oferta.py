from flask import Flask, request, session
from database.modelo import Modelo
import mysql.connector
from mysql.connector import Error
class Oferta():
    def __init__(self): 
        self.__productor=""
        self.__producto=""
        self.__fecha =""
    

    def registrar_oferta(self):
        try:
            self.__productor = session["id_usuario"]
            self.__producto = request.form["producto"]
            self.__fecha = request.form["fecha "]
            
            comandoSql = "INSERT INTO oferta(nombre, producto, fecha) values(%s, %s, %s)"
            data = [self.__productor,self.__producto, self.__fecha]
            baseDeDatos = Modelo(comandoSql,data,1)
            baseDeDatos.comando()
        except Error as err:
            return print(f"No se pudo registar la oferta{err}")
        finally:
            pass
    def buscar_oferta(self):
        try:
            self.__productor = session["id_productor"]
            self.__producto = request.form["producto"]
            self.__fecha = request.form["fecha "]
            
            comandoSql = "SELECT * FROM oferta WHERE producto LIKE %s AND WHERE fecha = %s"
            data = [self.__producto, self.__fecha]
            baseDeDatos = Modelo(comandoSql,data,0)
            resultadosDB = baseDeDatos.comando()
        except :
            resultadosDB = None
        finally:
            return resultadosDB       
      
    def buscar_ofertas_publicadas(self):
        try:
            self.__productor = session["id_productor"]
            
            comandoSql = "SELECT * FROM oferta WHERE productor = %s"
            data = [self.__productor]
            baseDeDatos = Modelo(comandoSql,data,0)
            resultadosDB = baseDeDatos.comando()
        except :
            resultadosDB = None
        finally:
            return resultadosDB  