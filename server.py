from flask import Flask


app = Flask(__name__)


@app.route('/')
def test():
	return 'Hello World'

@app.route('/welcome')
def welcomer():
	return 'Welcome'


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5000)