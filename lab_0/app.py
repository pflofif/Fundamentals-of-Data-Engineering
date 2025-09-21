import os
import psycopg2
from flask import Flask, render_template, request, redirect, url_for

def get_db_connection():
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    return conn

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users ORDER BY id;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        if name and email: 
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
            conn.commit()
            cur.close()
            conn.close()
            return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/edit/<int:user_id>', methods=('POST',))
def edit(user_id):
    name = request.form['name']
    email = request.form['email']

    if name and email:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('UPDATE users SET name = %s, email = %s WHERE id = %s', (name, email, user_id))
        conn.commit()
        cur.close()
        conn.close()

    return redirect(url_for('index'))


@app.route('/delete/<int:user_id>', methods=('POST',))
def delete(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE id = %s;', (user_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
