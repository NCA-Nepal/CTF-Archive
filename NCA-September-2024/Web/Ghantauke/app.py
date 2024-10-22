from flask import Flask, request, make_response, render_template
from hashlib import sha1

app = Flask(__name__)

# Define the flag
FLAG = 'nca{h3_15_6h4n74uk3_6uy555}'

@app.route('/', methods=['GET', 'POST'])
def index():
    # Retrieve headers and cookies
    dnt = request.headers.get('DNT', '0')  # Default to '0' if DNT is not set
    referer = request.headers.get('Referer', '')
    cookie = request.cookies.get('MasterCookie', '')

    # Level 1: User must visit from localhost
    if referer == '127.0.0.1':
        if dnt == '1':
            # Level 2: DNT must be enabled
            if cookie == sha1(b'nosk').hexdigest():
                # Level 3: Correct cookie (hash of "ctfmaster")
                if request.method == 'POST' and 'passcode' in request.form:
                    passcode = request.form['passcode']
                    if passcode.lower() == 'opensesame':
                        return render_template('index.html', message=f"GG! Here's the flag: {FLAG}")
                    else:
                        return render_template('index.html', message="🤖 Wrong passcode. You thought it was that easy?")
                elif request.method == 'GET' and 'passcode' in request.args:
                    passcode = request.args.get('passcode')
                    if passcode.lower() == 'opensesame':
                        return render_template('index.html', message=f"GG! Here's the flag: {FLAG}")
                    else:
                        return render_template('index.html', message="🤖 Incorrect passcode on GET request! Try again...")
                else:
                    return render_template('index.html', message="Hmmm... passcode? Still something's missing.", hint="Hint: passcode might be something treasure-opening phrase 🧙‍♂️")
            else:
                # Incorrect cookie or missing cookie
                return render_template('index.html', message="The key to the kingdom is missing... Ever heard of SHA1 hash? Hash 'nosk' and send it as 'MasterCookie'.")
        else:
            # DNT is not set
            return render_template('index.html', message="You are being watched 👀.")
    else:
        # Referer is not localhost
        return render_template('index.html', message="You aren't coming from 'home'! You're lost in the matrix...")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
