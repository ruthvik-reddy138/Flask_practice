from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if len(password)>6:
        error = "Password must not be greater than 6 characters."
    elif len(password)<6:
        error ="password must not be less than 6 characters"
        return render_template('login.html', error=error)

    return render_template('welcome.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
