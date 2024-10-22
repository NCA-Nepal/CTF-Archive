from flask import Flask, render_template, request, redirect, url_for, session, make_response
import sqlite3
import os
import base64

app = Flask(__name__)
app.secret_key = os.urandom(16)

SECRET_KEY = b'THIS_IS_SECURED_SECRET_KEY_I_GUESS_LMAO'

def xor(data, key):
    return bytes(a ^ b for a, b in zip(data, key * (len(data) // len(key) + 1)))

def create_token(username, uid):
    token_data = f'{{"username": "{username}", "uid": {uid}}}'.encode()
    encrypted_token = xor(token_data, SECRET_KEY)
    return base64.b64encode(encrypted_token).decode()

def decode_token(token):
    encrypted_token = base64.b64decode(token)
    decrypted_token = xor(encrypted_token, SECRET_KEY)
    return decrypted_token.decode()

def get_db_connection():
    conn = sqlite3.connect('ctf.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('dummy.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin':
            return "Username 'admin' is already taken.", 400
        
        conn = get_db_connection()
        conn.execute("INSERT INTO users (username, password, uid) VALUES (?, ?, ?)",
                     (username, password, 1))
        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()

        if user:
            token = create_token(user['username'], user['uid'])
            response = make_response(redirect(url_for('dashboard')))
            response.set_cookie('auth_token', token)
            return response
        else:
            return "Invalid credentials", 403

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    auth_token = request.cookies.get('auth_token')

    if not auth_token:
        return redirect(url_for('login'))

    try:
        user_info = decode_token(auth_token)
        # the uid is 0 below
        if '"uid": 0' in user_info:
            return "nca{d3v_ko_3p1c_61i7ch_l3_b1g4ry0}"
        else:
            return "What are you looking for? The flag? :D"
    except Exception:
        return "Invalid token", 400

if __name__ == '__main__':
    app.run(debug=False)
