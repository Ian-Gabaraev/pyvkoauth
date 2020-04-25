import requests
from access.conf import *


class AccessToken:
	@staticmethod
	def get(code):
		response = requests.get(access_token_uri+code)
		return response.json()['access_token']

	@staticmethod
	def is_valid(access_token):
		uri = api_call_uri % (
			'friends.get', 'fields=bdate', access_token, VK_OAUTH_VERSION)
		response = requests.get(uri)
		return 'error' in response.json().keys()


class UserInfo:
	def __init__(self, access_token):
		self.access_token = access_token
		self.user_first_name = None
		self.user_last_name = None
		self.user_friends = list()

	def collect_info(self):

		current_user_info = requests.get(
			api_call_uri % ('users.get', 'fields.bdate', 
				self.access_token, VK_OAUTH_VERSION))

		self.user_first_name = current_user_info.json()['response'][0]['first_name']
		self.user_last_name = current_user_info.json()['response'][0]['last_name']

		current_user_friends = requests.get(
			api_call_uri % ('friends.get', 'fields=bdate&count=5', 
				self.access_token, VK_OAUTH_VERSION))

		friends_first_names = [friend['first_name'] 
                               for friend in current_user_friends.json()['response']['items']]
		friends_last_names = [friend['last_name'] 
                              for friend in current_user_friends.json()['response']['items']]

		self.user_friends = list(zip(friends_first_names, friends_last_names))

	def get(self):
		self.collect_info()
		result = {
			'first_name' : self.user_first_name,
			'last_name' : self.user_last_name,
			'full_name' : {self.user_first_name} + ' ' + {self.user_last_name},
			'friends': self.user_friends,
		}
		return result

# print(UserInfo('7f160d5ec7fb1d89183afeff163e7f582629bbb954dde5c114fedcb4109d0b9128768cd933605ce423efd').get())