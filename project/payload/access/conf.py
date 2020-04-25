import os

APP_ID = os.environ['APP_ID']
HOST_W_SCHEMA = os.environ['HOST_W_SCHEMA']
REDIRECT_URI = os.environ['REDIRECT_URI']
SECRET = os.environ['SECRET']
RESPONSE_TYPE = os.environ['RESPONSE_TYPE']
DISPLAY = os.environ['DISPLAY']
SCOPE = os.environ['SCOPE']
VK_OAUTH_VERSION = os.environ['VK_OAUTH_VERSION']
SECRET_KEY = os.environ['FLASK_SECRET']

auth_uri = "%sauthorize?client_id=%s&display=%s&redirect_uri=%s&scope=%s&response_type=%s&v=%s" %(
			HOST_W_SCHEMA, APP_ID, DISPLAY, REDIRECT_URI, SCOPE, RESPONSE_TYPE, VK_OAUTH_VERSION)
access_token_uri = "%saccess_token?client_id=%s&client_secret=%s&redirect_uri=%s&code=" %(
			HOST_W_SCHEMA, APP_ID, SECRET, REDIRECT_URI)
api_call_uri = "https://api.vk.com/method/%s?%s&access_token=%s&v=%s"
