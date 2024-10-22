from flask import Flask, request, render_template, send_from_directory, redirect, url_for, Response
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        robot_id = request.form['robot_id']
        access_code = request.form['access_code']
        
        if robot_id == "fl4g" and access_code == "asudfgr3456_g1v3_m3_th3_fl4g_x435naslkjf":
            return render_template('flag.html', flag="nca{r0b0t_db_r41x4_h4i_k74_h0}")
        else:
            return render_template('login.html', error="Invalid credentials. Please try again.")
    return render_template('login.html')

@app.route('/robots.txt')
def robots():
    response = '''User-agent: *
Disallow: /robot-db/
    '''
    return Response(response, mimetype='text/plain')

@app.route('/robot-db/')
def download_database():
    return send_from_directory(directory=os.getcwd(), path='w0_robotdb.db', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
