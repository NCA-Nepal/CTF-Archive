from flask import Flask, render_template, request, redirect, url_for, make_response
import jwt
import datetime

app = Flask(__name__)

JWT_SECRET = "cybernepal"
JWT_ALGORITHM = "HS256"

USERS = {
    'admin': '23SDFG34t@$3ihfd2323@$@3',  # Admin credentials
    'guest': 'guest'
}

def create_token(username):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    token = jwt.encode({'username': username, 'exp': expiration}, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

@app.route('/')
def home():
    token = request.cookies.get('token')
    if token:
        try:
            data = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            if data['username'] == 'admin':
                return render_template('admin.html')
            elif data['username'] == 'guest':
                return render_template('guest.html')
        except jwt.ExpiredSignatureError:
            return "Session expired. Please log in again.", 401
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again.", 401
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in USERS and USERS[username] == password:
            token = create_token(username)
            resp = make_response(redirect(url_for('home')))
            resp.set_cookie('token', token)
            return resp
        else:
            return "Invalid credentials. Try again.", 401
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=False)
