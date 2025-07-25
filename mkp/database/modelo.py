import mysql.connector
#clase para la base de datos
class Modelo:
    #Atributos 
    def __init__(self, comandoSql,datos, confirmacion):
        self.__conexion = mysql.connector.connect(host="localhost",
                                                  user="pablito",
                                                  passwd="123456",
                                                  database="marketplace")
        self.__miCursor = self.__conexion.cursor()
        self.__comandoSql = comandoSql
        self.__datos = datos
        self.__confirmacion = confirmacion
        
    #Metodos 
    def comando(self):
        resultado = []        
        self.__miCursor.execute(self.__comandoSql, self.__datos)
        if self.__confirmacion == 1:
            self.__conexion.commit()
        else:
            resultado = self.__miCursor.fetchall()                
        self.__conexion.close()        
        return resultado

    def procedimiento(self,nombreProcedimiento,datos):
        self.__miCursor.callproc(nombreProcedimiento,datos)
        resultadosProcedimiento = self.__miCursor.stored_results()
        valorRecibido=[0]
        for resultado in resultadosProcedimiento:
            for dato in resultado:
                valorRecibido = dato
        self.__conexion.commit()  
        self.__conexion.close()
        return valorRecibido

