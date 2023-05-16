# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
app = Flask(__name__)
app.gps = ""


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/gps')
def get_gps():
    return f"{app.gps}"


@app.route('/setgps/<latlng>')
def get_the_gps(latlng):
    app.gps = latlng
    return "200"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
