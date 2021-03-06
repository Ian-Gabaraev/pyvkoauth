from sys import path
from flask import Markup, render_template, session, request, redirect, url_for
from flask import current_app as app
path.append('/Users/ian/Desktop/pauth/project/payload')
from user_info import AccessToken, UserInfo
from access.conf import auth_uri


@app.route('/pauth')
def index():
	"""
	To make the session survive
	browser closing, it shoud be made permenent
	"""
	session.parmenent = True
	if 'access_token' in session and AccessToken.is_valid(session.get('access_token')):
		response_payload = UserInfo(session.get('access_token')).get()
		return render_template('index.html', authorized=True, 
			username=response_payload['full_name'], friends = response_payload['friends'])
	else:
		return render_template('index.html', authorized=False, 
			username='guest', href=auth_uri)


@app.route('/pauth/reg')
def application():
	code = request.args.get('code', type=str)
	access_token = AccessToken.get(code)
	session['access_token'] = access_token
	return redirect(url_for('index'))
	
