# API-RESTful_taller3
Implementación de un API RESTful con Flask y PyMySQL

## 1. Descargar la carpeta comprimida:
   Al descargar la carpeta, la debemos descomprimir. La cual contiene los archivos, debe quedarnos de esta manera:
   
   ![image](https://github.com/user-attachments/assets/9568b931-a2e4-4fd5-bd0f-b63aa59cf70b)

## 2. Instalación de librerias Flask y PyMySQL.
   ```
   pip install Flask, PyMySQL
   ```
## 3. Activación del entorno virtual:
   ```
    python -m venv 'nombre_del_entorno_virtual' NOTA: En este caso es: api_taller3
    api_taller3\Scripts\activate
   ```

## 4. Ejecución para obtener el endpoint
   Se ejecuta la aplicación para obtener la ruta de acceso del endpoint:
   ```
    python app.py
   ```
   (EJEMPLO: GET http://127.0.0.1:5000/usuarios )



## 3. INFORMACIÓN:
   ```
   luego de a ver descomprimido la carpeta principal 'api_taller3'
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






   
  
