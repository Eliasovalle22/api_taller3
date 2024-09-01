from flask import Flask, jsonify, request
import pymysql.cursors

app = Flask(__name__)

# Configuración de la base de datos


def connection_mysql():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='api',
        cursorclass=pymysql.cursors.DictCursor)
    return connection


# Crear un usuario

@app.route('/usuarios', methods=['POST'])
def create_user():

    data = request.get_json()
    connection = connection_mysql()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (nombre, correo) VALUES (%s, %s)"
            cursor.execute(sql, (data['nombre'], data['correo']))
            result = cursor.fetchall()
        connection.commit()

    return jsonify({
        'Mensaje': 'creacion exitosa'
    }), 201


# Obtener todos los datos

@app.route('/usuarios', methods=['GET'])
def get_users():
    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = 'SELECT id, nombre, correo FROM users'
        cursor.execute(sql)
        result = cursor.fetchall()

        return jsonify({
            'Usuarios': result
        }), 200


# Obtener un usuario por su ID

@app.route('/usuarios/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM users WHERE id = %s'
        cursor.execute(sql, (user_id,))
        result = cursor.fetchone()

    if result:
        return jsonify(result), 200
    else:
        return jsonify({'Mensaje': 'Usuario no existe'}), 404


# Actualizar un usuario por ID

@app.route('/usuarios/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    nombre = data.get('nombre')
    correo = data.get('correo')

    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = "UPDATE users SET nombre = %s, correo = %s WHERE id = %s"
        cursor.execute(sql, (nombre, correo, user_id))
        connection.commit()

    return jsonify({'Mensaje': 'Usuario actualizado con exito'}), 200


# Eliminar un usuario por ID

@app.route('/usuarios/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = "DELETE FROM users WHERE id = %s"
        cursor.execute(sql, (user_id))
        connection.commit()

    return jsonify({'Mensaje': 'Usuario eliminado con exito'}), 200


# Crear un producto

@app.route('/productos', methods=['POST'])
def create_product():

    data = request.get_json()
    nombre = data.get('nombre')
    precio = data.get('precio')

    connection = connection_mysql()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO products (nombre, precio) VALUES (%s, %s)"
            cursor.execute(sql, (nombre, precio))
        connection.commit()

    return jsonify({
        'Mensaje': 'Producto creado con éxito'
    }), 201


# Obtener todos los productos

@app.route('/productos', methods=['GET'])
def get_products():
    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = 'SELECT id, nombre, precio FROM products'
        cursor.execute(sql)
        result = cursor.fetchall()

        return jsonify({
            'Productos': result
        }), 200


# Obtener un producto por su ID

@app.route('/productos/<int:product_id>', methods=['GET'])
def get_product(product_id):
    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM products WHERE id = %s'
        cursor.execute(sql, (product_id,))
        result = cursor.fetchone()

    if result:
        return jsonify(result), 200
    else:
        return jsonify({'Mensaje': 'Producto no existe'}), 404


# Actualizar un Producto por ID

@app.route('/productos/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    nombre = data.get('nombre')
    precio = data.get('precio')

    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = "UPDATE products SET nombre = %s, precio = %s WHERE id = %s"
        cursor.execute(sql, (nombre, precio, product_id))
        connection.commit()

    return jsonify({'Mensaje': 'Producto actualizado con exito'}), 200


# Eliminar un producto por ID

@app.route('/productos/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    connection = connection_mysql()
    with connection.cursor() as cursor:
        sql = "DELETE FROM products WHERE id = %s"
        cursor.execute(sql, (product_id,))
        connection.commit()

    return jsonify({'Mensaje': 'Producto eliminado con exito'}), 200


if __name__ == '__main__':
    app.run(debug=True)


