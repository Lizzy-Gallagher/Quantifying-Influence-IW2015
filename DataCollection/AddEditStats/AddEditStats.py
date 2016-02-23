import csv
from datetime import datetime
import requests
from DataCollection.User import User

__author__ = 'lizzybradley'


class AddEditStats:
	user_list = []

	def __init__(self, csv_filename):
		self.csv_filename = csv_filename
		self.filename = csv_filename[:-4]

		with open(csv_filename) as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:
				user = User(row)
				self.user_list.append(user)

	def collect_edits(self):
		i = 0
		for user in self.user_list[0:50]:
			print i
			i += 1

			username = user.username
			election_date = datetime.strptime(user.election_date, '%Y-%m-%d %H:%M:%S')

			user.minor_edits = self.collect_minor_edits(username, election_date)
			user.nonminor_edits, user.revert_edits, user.large_edits = self.collect_reg_edits(username, election_date)

			with open('data.csv', 'a') as file_:
				file_.write(str(user))
				file_.write('\n')

	def collect_minor_edits(self, username, election_date):
		stop_date = election_date.isoformat('T') + 'Z'
		isPaging = True

		minor_edits = 0

		url = "https://en.wikipedia.org/w/api.php?action=query&list=usercontribs&uclimit=500&format=json" + \
			"&ucshow=minor&ucprop=comment|size|flags|sizediff|timestamp&ucdir=newer" + \
			"&ucuser=" + username + "&ucend=" + stop_date
		url = url.replace(' ', '+')

		while isPaging:
			r = requests.get(url)
			try:
				contribs = 0

				# Check if already complete
				possible_contribs = len(r.json()['query']['usercontribs'])
				last_timestamp = r.json()['query']['usercontribs'][possible_contribs - 1]['timestamp']
				last_datetime = datetime.strptime(last_timestamp, '%Y-%m-%dT%H:%M:%SZ')

				if last_datetime < election_date:
					contribs = possible_contribs

				else:
					for contrib in r.json()['query']['usercontribs']:
						contrib_timestamp = datetime.strptime(contrib['timestamp'], '%Y-%m-%dT%H:%M:%SZ')
						if contrib_timestamp < election_date:
							contribs += 1
						else:
							isPaging = False
							break

				minor_edits += contribs

				uccontinue = r.json()['continue']['uccontinue']
				url = "https://en.wikipedia.org/w/api.php?action=query&list=usercontribs&uclimit=500&format=json" + \
					  "&ucshow=minor&ucprop=comment|size|flags|sizediff|timestamp&ucdir=newer" + \
					  "&ucuser=" + username + "&ucend=" + stop_date + "&uccontinue=" + uccontinue
			except:
				isPaging = False

		return minor_edits

	def collect_reg_edits(self, username, election_date):
		stop_date = election_date.isoformat('T') + 'Z'
		isPaging = True

		nonminor_edits = 0
		revert_edits   = 0
		large_edits    = 0

		url = "https://en.wikipedia.org/w/api.php?action=query&list=usercontribs&uclimit=500&format=json" + \
			  "&ucshow=!minor&ucprop=comment|size|flags|sizediff|timestamp&ucdir=newer" + \
			  "&ucuser=" + username + "&ucend=" + stop_date
		url = url.replace(' ', '+')

		while isPaging:
			r = requests.get(url)
			try:
				for contrib in r.json()['query']['usercontribs']:
					contrib_timestamp = datetime.strptime(contrib['timestamp'], '%Y-%m-%dT%H:%M:%SZ')
					if contrib_timestamp < election_date:
						nonminor_edits += 1
						if 'revert' in contrib['comment'] or 'revision' in contrib['comment'] \
								or 'Revert' in contrib['comment'] or 'Revision' in contrib['comment']:
							revert_edits += 1
						elif abs(int(contrib['sizediff'])) > 500:
							large_edits += 1
					else:
						isPaging = False
						break

				uccontinue = r.json()['continue']['uccontinue']
				url = "https://en.wikipedia.org/w/api.php?action=query&list=usercontribs&uclimit=500&format=json" + \
					  "&ucshow=!minor&ucprop=comment|size|flags|sizediff|timestamp&ucdir=newer" + \
					  "&ucuser=" + username + "&ucend=" + stop_date + "&uccontinue=" + uccontinue
			except:
				isPaging = False

		return nonminor_edits, revert_edits, large_edits

edit_stats = AddEditStats('../../Data/17_images.csv')
edit_stats.collect_edits()

# bot_edits   = 0 # marked with "b"
