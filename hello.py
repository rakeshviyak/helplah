from flask import Flask, render_template, request
import requests

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
    type = request.args.get('type')
    when = request.args.get('when')
    url = "https://api.goroost.com/api/push"

    payload = "{\"alert\":\"Help needed\", \"url\":\"https://helplah.herokuapp.com/notify?when="+when+"&type="+type+"\"}"
    headers = {
        'content-type': "application/json",
        'authorization': "Basic enR2Y29nYTg2ZDhrbWk5ampxOHZwcmd6eGNhaGxrNTA6a3VkdXEyeTJtNmo1cjI0MGVidzd6Yjh1NnZ2NHAzM3U="
        # 'access-control-allow-origin': "*"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
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