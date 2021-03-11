import os
import json
import program as p

from flask import Flask, request, session, redirect, url_for

from werkzeug.exceptions import HTTPException

from datetime import timedelta

app = Flask(__name__)
app.secret_key = "fa-python-rs"
app.permanent_session_lifetime =  timedelta(hours=1)


@app.errorhandler(Exception)
def handle_exception(e):
	return p.response(0, str(e))
	

@app.route('/api/fa', methods = ['GET'])
def index():
	if 'ip' not in session:
		return p.response(0, "You are not logged")
	return p.response(1, "Logged in as " + session['ip'])
	

@app.route('/api/fa/init', methods = ['GET'])
def session_init():
	session['ip'] = request.remote_addr
	session['model'] = None
	session.permanent = True
	return p.response(1, "initialization succeeded!")
	
	
@app.route('/api/fa/destroy', methods = ['GET'])
def session_destroy():
	if 'ip' not in session:
		return p.response(0, "You are not logged")
	session.pop('ip', None)
	session.pop('model', None)
	return p.response(1, "destroying succeeded!")
	

@app.route('/api/fa/dfa/setup', methods=['POST'])
def dfa_setup():
	if 'ip' not in session:
		return p.response(0, "You are not logged")
	data = request.get_json()
	assert data is not None and data['type'] == "dfa", "JSON object mismatched"
	session['model'] = data
	return p.response(1, "setup succeeded!")
	
	
@app.route('/api/fa/dfa/exec', methods=['POST'])
def dfa_exec():
	if 'ip' not in session:
		return p.response(0, "You are not logged")
	model = session.get('model')
	string = request.args.get('string')
	assert model is not None and model['type'] == "dfa", "JSON object mismatched"
	return p.response(1, p.dfa_exec(model, string))
	
	
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)


