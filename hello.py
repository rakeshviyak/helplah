from flask import Flask, render_template


app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('config_development.py', silent=True)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/find')
def find():
    return render_template('find.html')


@app.route('/leadership')
def leadership():
    return render_template('leadership.html')


@app.route('/matched')
def matched():
    return render_template('matched.html')

@app.route('/roost')
def roost():
    return render_template('roost.html')


@app.route('/roost.html')
def roosthtml():
    return render_template('roost.html')


@app.route('/notify')
def notify():
    return render_template('notify.html', onemap_apikey=app.config['ONEMAP_APIKEY'])


if __name__ == '__main__':
    app.run(debug=True)