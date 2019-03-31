from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
from flask_sockets import Sockets
import datetime
import time

app = Flask(__name__, static_url_path='/static')
sockets = Sockets(app)
FILE_INFO = "file.txt"

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")



@sockets.route('/echo')
def echo_socket(ws):
	while True:
		try:
			#message = ws.receive()
			ws.send(open(FILE_INFO).read())
			time.sleep(.1)
		except Exception as exp:
			print exp
			pass

@app.route('/map', methods=['GET'])
def maps():
	return render_template("map.html")

@app.route('/echo_test', methods=['GET'])
def echo_test():
	return render_template('example.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)
