import csv
from datetime import datetime

import requests

from DataCollection.User import User

__author__ = 'lizzybradley'

class AddDaysActive:
	user_list = []

	def __init__(self, filename):
		with open(filename) as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:
				self.user_list.append(User(row))

	def add(self):
		for user in self.user_list:
			username = user.username.replace(" ", "%20").replace("&", "%26").replace("-", "%2D")

			url = "https://en.wikipedia.org/w/api.php?action=query&list=usercontribs&format" + \
				  "=json&uclimit=1&ucuser={0}&ucdir=newer".format(username)

			r = requests.get(url)
			try :
				first_edit_timestamp = r.json()['query']['usercontribs'][0]['timestamp'][:len('YYYY-MM-DD')]
				first_edit_date = datetime.strptime(first_edit_timestamp, '%Y-%m-%d')

				election_date = datetime.strptime(user.date_of_election, '%Y-%m-%d %H:%M:%S')
				days_active = abs((first_edit_date - election_date).days)
			except:
				days_active = 0

			user.days_active = days_active

			print user

add_days_active = AddDaysActive('../Data/7_metadata.csv')
add_days_active.add()
