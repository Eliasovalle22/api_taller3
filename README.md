# API-RESTful_taller3
Implementación de un API RESTful con Flask y PyMySQL

## Descargar la carpeta comprimida:
1. Descomprimir la carpeta principal.
   ```
   RECOMENDACIÓN: luego de a ver descomprimido la carpeta principal 'api_taller3'
    debemos cortar  la carpeta llamada 'bd_api_taller3.sql' y pegarla a fuera de la carpeta principal
    la cual contiene el SCRIPT de la base de datos creada
   para evitar errores al ejecutar el aplicativo
   ```
## NOTA:
La base de datos cuenta con una contraseña
 ```
        host='localhost',
        user='root',
        password='1234',
        database='api',
 ```
   
## Instalació de recursos Flask y PyMySQL

2. Activa el entorno virtual e instalar las librerias:
    ```
    python -m venv 'nombre_del_entorno_virtual' NOTA: En este caso es: api_taller3
    api_taller3\Scripts\activate  # Para Windows
    pip install Flask, PyMySQL
    ```
## Uso
3. Creamos un archivo en el cual pondremos todo el codigo:
   ```
    'nombre_del_archivo' NOTA: En este caso es: app.py
   ```
## Ejecución para obtener el ENDPOINT
4. Se ejecuta la aplicación para obtener la ruta de acceso del endpoint:
   ```
    python app.py
   ```
   Se ejecuta la ruta del endpoint (EJEMPLO: GET http://127.0.0.1:5000/usuarios )


## NOTA MUY IMPORTANT:
5. Se debe tener conocimiento de como funciona la implementación de datos con POSTMAN, para que la implementaciones CRUD (Crear, Leer, Actualizar, Eliminar) se realicen con exito.

## Si presentas inconvenientes al realizar el procedimiento por favor comunicate conmigo
  ```
  Ramón Montesino 3128789705
  ```






   
  
