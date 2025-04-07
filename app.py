import os
import json
from flask import Flask, jsonify
from pymongo import MongoClient
from urllib.parse import quote_plus  # Para codificar la contraseña en la URL
from dotenv import load_dotenv  # Para cargar las variables de entorno

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Configura la conexión a MongoDB Atlas usando variables de entorno
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
cluster_url = os.getenv("MONGO_CLUSTER_URL")
database_name = os.getenv("MONGO_DATABASE_NAME")

# Verificar que las variables de entorno se cargaron correctamente
if not all([username, password, cluster_url, database_name]):
    print("Error: Una o más variables de entorno no están configuradas correctamente.")
    exit(1)

# Codifica la contraseña para que sea segura en la URL
encoded_password = quote_plus(password)

# Cadena de conexión
connection_string = f"mongodb+srv://{username}:{encoded_password}@{cluster_url}/?retryWrites=true&w=majority"

# Conectar a MongoDB con manejo de errores
try:
    client = MongoClient(connection_string)
    db = client[database_name]
    client.admin.command('ping')  # Prueba de conexión
    print("Conectado exitosamente a MongoDB Atlas")
except Exception as e:
    print(f"Error al conectar a MongoDB: {e}")
    exit(1)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Bienvenido a la API. Usa /export-all para exportar las colecciones.'}), 200

@app.route('/export-all', methods=['GET'])
def export_all_collections():
    try:
        # Obtener todas las colecciones en la base de datos
        collections = db.list_collection_names()

        # Ruta base para guardar los archivos
        export_folder = r"C:\Users\luisa\OneDrive\Escritorio\Proyecto\PowerBI"

        # Crear la carpeta si no existe (aunque en este caso ya debería existir)
        os.makedirs(export_folder, exist_ok=True)

        # Exportar cada colección
        for collection_name in collections:
            try:
                collection = db[collection_name]
                data = list(collection.find({}, {'_id': 0}))  # Excluye el campo _id

                # Ruta del archivo JSON
                file_path = os.path.join(export_folder, f"{collection_name}.json")

                # Guardar los datos en un archivo JSON
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
            except Exception as e:
                print(f"Error al exportar la colección {collection_name}: {e}")

        return jsonify({'message': f'Todas las colecciones exportadas a {export_folder}'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Cambia el puerto aquí si es necesario