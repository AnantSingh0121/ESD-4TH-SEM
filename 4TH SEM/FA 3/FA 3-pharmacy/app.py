from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = 'my precious'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'esd_grp. 9'

mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM medicine")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', medicine=data)


@app.route('/insert', methods = ['POST'])
def insert():
        flash("Data Inserted Successfully")
        name = request.form.get('name')
        email = request.form.get('email')
        payment = request.form.get('payment')
        phone = request.form.get('phone')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO medicine (name, email, payment, phone) VALUES (%s, %s, %s, %s)", (name, email, payment, phone))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully !!!!!!!!!!!!")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM medicine WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))

@app.route('/update', methods=['POST'])
def update():
    id = request.form['id']
    name = request.form['name']
    email = request.form['email']
    payment = request.form['payment']
    phone = request.form['phone']
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE medicine 
        SET name=%s, email=%s, payment=%s, phone=%s 
        WHERE id=%s
    """, (name, email, payment, phone, id))
    mysql.connection.commit()
    flash('Data Updated Successfully')
    return redirect(url_for('Index'))




if __name__ == "__main__":
    app.run(debug=True)
