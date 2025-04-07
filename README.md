# Exportador de Datos MongoDB para Análisis en Power BI 🚀

Este proyecto es la **primera parte** de una solución diseñada para facilitar el análisis de datos en **Power BI**. La herramienta permite exportar colecciones de una base de datos **MongoDB Atlas** a archivos JSON, que luego pueden ser utilizados en Power BI para la toma de decisiones basada en datos.

---

## 🌟 Características

- **Conexión segura a MongoDB Atlas**: Configuración mediante variables de entorno para proteger credenciales sensibles.
- **Exportación de colecciones**: Exporta todas las colecciones de una base de datos MongoDB a archivos JSON.
- **Preparación para Power BI**: Los datos exportados están listos para ser cargados y analizados en Power BI.
- **Fácil de usar**: Una API RESTful simple que automatiza el proceso de exportación.
- **Código modular y extensible**: Ideal para aprender y expandir en futuros proyectos.

---

## 🛠️ Requisitos previos

Antes de comenzar, asegúrate de tener lo siguiente instalado en tu máquina:

- **Python 3.8 o superior**.
- **MongoDB Atlas** configurado con una base de datos y colecciones.
- **Postman** o un navegador para probar la API.
- **Power BI Desktop** para cargar y analizar los datos exportados.
- **Dependencias de Python**:
  - Flask
  - PyMongo
  - python-dotenv

Instala las dependencias con:
```bash
pip install flask pymongo python-dotenv

🚀 Cómo usar
1. Clona este repositorio
git clone https://github.com/tu-usuario/exportador-mongodb-powerbi.git
cd exportador-mongodb-powerbi

2. Configura las credenciales de MongoDB
Crea un archivo .env en la raíz del proyecto con las siguientes variables (reemplaza con tus credenciales reales):
MONGO_USERNAME=tu_usuario
MONGO_PASSWORD=tu_contraseña
MONGO_CLUSTER_URL=tu_cluster.mongodb.net
MONGO_DATABASE_NAME=nombre_de_tu_base_de_datos

3. Ejecuta el servidor Flask
Inicia el servidor con:

python [app.py](http://_vscodecontentref_/1)

Deberías ver un mensaje como este:
Conectado exitosamente a MongoDB Atlas
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

4. Exporta las colecciones
  Abre tu navegador o Postman y accede a:
    * Ruta raíz: http://127.0.0.1:5000/ para ver el mensaje de bienvenida.
    * Exportar colecciones: http://127.0.0.1:5000/export-all para exportar todas las colecciones.

5. Verifica los archivos exportados
Los archivos JSON se guardarán en la carpeta:
C:\Users\nombre\OneDrive\Escritorio

6. Carga los datos en Power BI
 Abre Power BI Desktop.
 Selecciona Obtener datos > JSON.
 Carga los archivos exportados y comienza tu análisis.

 
GitHub Copilot
Aquí tienes un README.md completo y profesional para tu proyecto, enfocado en la exportación de datos desde MongoDB para su análisis en Power BI:

🚀 Cómo usar
1. Clona este repositorio
2. Configura las credenciales de MongoDB
Crea un archivo .env en la raíz del proyecto con las siguientes variables (reemplaza con tus credenciales reales):

3. Ejecuta el servidor Flask
Inicia el servidor con:

Deberías ver un mensaje como este:

4. Exporta las colecciones
Abre tu navegador o Postman y accede a:
Ruta raíz: http://127.0.0.1:5000/ para ver el mensaje de bienvenida.
Exportar colecciones: http://127.0.0.1:5000/export-all para exportar todas las colecciones.
5. Verifica los archivos exportados
Los archivos JSON se guardarán en la carpeta:

6. Carga los datos en Power BI
Abre Power BI Desktop.
Selecciona Obtener datos > JSON.
Carga los archivos exportados y comienza tu análisis.

📂 Estructura del proyecto
Proyecto/
│
├── [app.py](http://_vscodecontentref_/2)          # Código principal de la API Flask
├── .env            # Archivo con credenciales sensibles (no se sube al repositorio)
├── .gitignore      # Ignora archivos sensibles como .env
├── [README.md](http://_vscodecontentref_/3)       # Documentación del proyecto
└── [requirements.txt](http://_vscodecontentref_/4) # Dependencias del proyecto (opcional)

🌈 Ejemplo de uso
1. Mensaje de bienvenida
Accede a http://127.0.0.1:5000/ y verás:

{
  "message": "Bienvenido a la API. Usa /export-all para exportar las colecciones."
}

2. Exportar colecciones
Accede a http://127.0.0.1:5000/export-all y verás:

{
  "message": "Todas las colecciones exportadas a C:\\Users\\luisa\\OneDrive\\Escritorio"
}

🧠 ¿Qué aprenderás con este proyecto?
Cómo conectar una aplicación Flask a MongoDB Atlas.
Cómo exportar datos de MongoDB a archivos JSON.
Cómo preparar datos para su análisis en Power BI.
Buenas prácticas para proteger credenciales con variables de entorno.

📌 Próximos pasos
Este proyecto es solo el comienzo. Algunas ideas para expandirlo:

Exportación selectiva: Agregar una ruta para exportar colecciones específicas.
Transformación de datos: Preprocesar los datos antes de exportarlos.
Integración con Power BI: Automatizar la carga de datos en Power BI.
Autenticación: Proteger la API con un sistema de autenticación.

🤝 Contribuciones
¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este proyecto, no dudes en abrir un issue o enviar un pull request.

📝 Licencia
Este proyecto está bajo la licencia MIT. Siéntete libre de usarlo y modificarlo según tus necesidades.

💌 Agradecimientos
Gracias por interesarte en este proyecto. Espero que te sea útil y que inspire tus análisis en Power BI. ¡El conocimiento basado en datos es el futuro! 🚀

---

### ¿Qué incluye este README?
1. **Introducción clara**: Explica el propósito del proyecto y su relación con Power BI.
2. **Características destacadas**: Resalta lo que hace especial al proyecto.
3. **Instrucciones detalladas**: Paso a paso para configurar y usar la herramienta.
4. **Estructura del proyecto**: Ayuda a entender cómo está organizado.
5. **Ejemplo de uso**: Muestra cómo interactuar con la API.
6. **Próximos pasos**: Ideas para expandir el proyecto.
7. **Agradecimientos**: Un toque personal para conectar con el lector.

Este README está diseñado para captar la atención y guiar a los usuarios de manera efectiva. ¡Espero que te ayude a presentar tu proyecto de manera profesional y atractiva! 😊