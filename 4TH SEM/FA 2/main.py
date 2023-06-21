import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from contextlib import closing


@app.route('/create', methods=['POST'])
def create_customer():
    try:
        _json = request.json
        _id = _json['id']
        _name = _json['name']
        _email = _json['email']
        _phone = _json['phone']
        _address = _json['address']
        if _id and _name and _email and _phone and _address and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO customer(id, name, email, phone, address) VALUES(%s, %s, %s, %s, %s)"
            bindData = (_id, _name, _email, _phone, _address)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('User added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage("User added not successfully")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/customer')
def customer():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, name, email, phone, address FROM customer")
        customerRows = cursor.fetchall()
        respone = jsonify(customerRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/customer/<int:id>')
def customer_details(customer_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, name, email, phone, address FROM customer WHERE id =%s", id)
        customerRow = cursor.fetchone()
        respone = jsonify(customerRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/users/<int:id>', methods=['PUT'])
def update_customer():
    try:
        _json = request.json
        _id = _json['id']
        _name = _json['name']
        _email = _json['email']
        _phone = _json['phone']
        _address = _json['address']
        if _name and _email and _phone and _address and _id and request.method == 'PUT':
            sqlQuery = "UPDATE customer SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
            bindData = (_name, _email, _phone, _address, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('User updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage('User not updated successfully!')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_customer(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customer WHERE id =%s", (id,))
        conn.commit()
        respone = jsonify('User deleted successfully!')
        respone.status_code = 200
        return respone
    
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone


if __name__ == "__main__":
    app.run()
    
    


# import pymysql
# from app import app
# from config import mysql
# from flask import jsonify
# from flask import flash, request
# from contextlib import closing

# @app.route('/create', methods=['POST'])
# def create_customer():
#     try:
#         _json = request.json
#         _name = _json['name']
#         _email = _json['email']
#         _phone = _json['phone']
#         _address = _json['address']
#         if _name and _email and _phone and _address and request.method == 'POST':
#             conn = mysql.connect()
#             cursor = conn.cursor(pymysql.cursors.DictCursor)
#             sqlQuery = "INSERT INTO customer(name, email, phone, address) VALUES(%s, %s, %s, %s)"
#             bindData = (_name, _email, _phone, _address)
#             cursor.execute(sqlQuery, bindData)
#             conn.commit()
#             respone = jsonify('User added successfully!')
#             respone.status_code = 200
#             return respone
#         else:
#             return showMessage("User not added successfully")
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()


# @app.route('/customer')
# def customer():
#     try:
#         conn = mysql.connect()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         cursor.execute("SELECT id, name, email, phone, address FROM customer")
#         customerRows = cursor.fetchall()
#         respone = jsonify(customerRows)
#         respone.status_code = 200
#         return respone
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()


# @app.route('/customer/<int:customer_id>')
# def customer_details(customer_id):
#     try:
#         conn = mysql.connect()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         cursor.execute("SELECT id, name, email, phone, address FROM customer WHERE id =%s", customer_id)
#         customerRow = cursor.fetchone()
#         respone = jsonify(customerRow)
#         respone.status_code = 200
#         return respone
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()


# @app.route('/update', methods=['PUT'])
# def update_customer():
#     try:
#         _json = request.json
#         _id = _json['id']
#         _name = _json['name']
#         _email = _json['email']
#         _phone = _json['phone']
#         _address = _json['address']
#         if _name and _email and _phone and _address and _id and request.method == 'PUT':
#             sqlQuery = "UPDATE customer SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
#             bindData = (_name, _email, _phone, _address, _id,)
#             conn = mysql.connect()
#             cursor = conn.cursor()
#             cursor.execute(sqlQuery, bindData)
#             conn.commit()
#             respone = jsonify('User updated successfully!')
#             respone.status_code = 200
#             return respone
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()


# @app.route('/delete/<int:id>', methods=['DELETE'])
# def delete_customer(id):
#     try:
#         conn = mysql.connect()
#         cursor = conn.cursor()
#         cursor.execute("DELETE FROM customer WHERE id =%s", (id,))
#         conn.commit()
#         respone = jsonify('User deleted successfully!')
#         respone.status_code = 200
#         return respone
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()


# @app.errorhandler(404)
# def showMessage(error=None):
#     message = {
#         'status': 404,
#         'message': 'Record not found: ' + request.url,
#     }
#     respone = jsonify(message)
#     respone.status_code = 404
#     return respone


# if __name__ == "__main__":
#     app.run(debug=True)