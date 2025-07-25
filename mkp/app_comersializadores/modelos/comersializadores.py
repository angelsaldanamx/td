
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import requests
from werkzeug.exceptions import BadRequest
from datetime import datetime

# Parámetro faltante para las rutas a la API
API_URL = "http://localhost:5000"  # Cambia esto por la URL real de tu API

#este bloque de codigo lo hizo jose manuel
app = Flask(__name__)

@app.route('/menu')
def menu():
    return render_template('menu_Diego.html')

#blique de codigo de alexis
@app.route('/buscar_demanda', methods=['POST'])
def buscar_demanda():
    try:
        data = {
            'nombre': request.form['nombre']
        }
        response = requests.post(f"{API_URL}/buscar_demanda", json=data)
        response.raise_for_status()
        return render_template('mostrar.html', datos=response.json())
    except Exception as e:
        flash(f'Error al buscar demanda: {str(e)}')
        return redirect(url_for('menu'))

#bloque de codigo de jares

@app.route('/autenticacion', methods=['POST'])
def autenticacion():
    try:
        # Obtener datos del formulario
        usuario = request.form['usuario']
        password = request.form['password']

        # Preparar datos para la API
        data = {
            'usuario': usuario,
            'password': password
        }

        # Hacer la petición a la API de autenticación
        response = requests.post(f"{API_URL}/autenticacion", json=data)
        response.raise_for_status()  # Lanza excepción para respuestas HTTP no exitosas

        # Si la autenticación es exitosa, redirigir al menú
        if response.json().get('autenticado'):
            return redirect(url_for('menu'))
        else:
            flash('Usuario o contraseña incorrectos')
            return redirect(url_for('login'))

    except KeyError as e:
        flash(f'Faltan campos obligatorios: {e}')
        return redirect(url_for('login'))
    except requests.exceptions.RequestException as e:
        flash(f'Error al conectar con el servidor: {str(e)}')
        return redirect(url_for('login'))
    except BadRequest:
        flash('Error en la solicitud')
        return redirect(url_for('login'))
    except Exception as e:
        flash(f'Error inesperado: {str(e)}')
        return redirect(url_for('login'))


#bloque de codigo de abigail

@app.route('/buscar_demandas_publicadas', methods=['GET'])
def buscar_demandas_publicadas():
    try:
        # Obtener parámetros de consulta (si los hay)
        productor_id = request.args.get('productor_id')
        vigentes = request.args.get('vigentes', 'true').lower() == 'true'

        # Construir parámetros para la API
        params = {}
        if productor_id:
            params['productor_id'] = productor_id
        if vigentes:
            params['fecha_actual'] = datetime.now().isoformat()

        # Hacer la petición a la API
        response = requests.get(f"{API_URL}/demandas", params=params)
        response.raise_for_status()  # Lanza excepción para respuestas HTTP no exitosas

        # Retornar los resultados
        return jsonify({
            'success': True,
            'demandas': response.json(),
            'count': len(response.json())
        })

    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': f'Error al conectar con el servidor: {str(e)}'
        }), 500
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error inesperado: {str(e)}'
        }), 500
        
#bloque de codigo de yuliana
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar_cliente', methods=['POST'])
def agregar_cliente():
    try:
        data = {
            "nombre": request.form['nombre'],
            "usuario": request.form['usuario'],
            "password": request.form['password'],
            "correo": request.form['correo'],
            "telefono": request.form['telefono']
        }

        print("Cliente registrado correctamente:")
        print(data)

        return redirect('/')
    except Exception as e:
        return f"Ocurrió un error: {str(e)}"


