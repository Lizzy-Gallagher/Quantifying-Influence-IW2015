import csv

import requests

from DataCollection.User import User

__author__ = 'lizzybradley'

# Add gender and emailable

class AddMetadata:
	user_list = []

	def __init__(self, filename):
		with open(filename) as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:
				self.user_list.append(User(row))

	def add(self):
		for user in self.user_list[:]:
			username = user.username.replace(" ", "%20").replace("&", "%26")

			url = "https://en.wikipedia.org/w/api.php?action=query&list=users&" + \
				   "format=json&usprop=emailable%7Cgender&ususers=" + username

			r = requests.get(url)
			gender = r.json()['query']['users'][0]['gender']
			try:
				emailable = len(r.json()['query']['users'][0]['emailable']) > 0
			except:
				emailable = False

			user.gender = gender

			if emailable:
				user.emailable = 1
			else:
				user.emailable = 0

			print user

add_metadata = AddMetadata('../Data/6_total_edits.csv')
add_metadata.add()