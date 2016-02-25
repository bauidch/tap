from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World! Welcome to Flask and Dokku'
	
@app.route('/dokku')
def dokku():
    return 'Dokku is a mini PaaS with Docker'	


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
