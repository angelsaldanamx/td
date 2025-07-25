from flask import Flask, render_template, request,session
from clases.comercializadores import Comercializadores
from clases.productores import Productores
from clases.oferta import Oferta
from clases.demanda import Demanda
app = Flask(__name__)
app.secret_key = 'Uppenjamo_2025'

@app.route('/')
def index(): 
    session["usuario"] = ""
    session["id_usuario"] = ""
    return render_template('index.html')

@app.route('/formulario_registro')
def registro(): 
    return render_template('registro.html')

@app.route('/menu')
def menu(): 
    return render_template('menu.html')

@app.route('/autenticacion', methods=['POST'])
def autenticacion():
    comercializador = Comercializadores()
    datosUsuario = comercializador.autenticacion()
    if not datosUsuario:
        return render_template('index.html',mensaje = 'usuario o contraseña incorrecta')
    else: 
       session ["id_usuario"]  = datosUsuario[0][0]
       session ["usuario"]  = datosUsuario[0][1]
       return render_template ('menu.html')


@app.route('/procesar_registro', methods=['POST'])
def procesar_registro(): 
    comercializador = Comercializador()
    comercializador.procesar_registro()
    
@app.route('/buscar_oferta')
def buscar_oferta():
    return render_template ('buscar_oferta.html')

@app.route('/registrar_demanda')
def registrar_demanda():
    return render_template ('registrar_demanda.html')

@app.route('/procesar_registro_demanda',methods=['POST'])
def procesar_registro_demanda():
    demanda = Demanda()
    demanda.registrar_demanda()
    respuesta = demanda.buscar_demandas_publicadas()
    return render_template('mostrar_demanda_publicada.html', demanda_data = respuesta)   
    
@app.route('/mostrar_demandas_publicadas')
def mostrar_demandas_publicadas():
    demanda = Demanda()
    respuesta = demanda.buscar_demandas_publicadas()
    return render_template('mostrar_demanda_publicada.html', demanda_data = respuesta)
    

if __name__ == '__main__':
    app.run(debug=True)
