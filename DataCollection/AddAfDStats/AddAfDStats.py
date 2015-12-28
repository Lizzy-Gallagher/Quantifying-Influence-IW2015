import csv
from bs4 import BeautifulSoup
import requests
from DataCollection.User import User
from datetime import datetime

__author__ = 'lizzybradley'

class AddAfDStats:
	user_list = []

	def __init__(self, filename):
		with open(filename) as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:
				self.user_list.append(User(row))

	def add(self):
		for user in self.user_list[3000:3100]:
			username = user.username.replace(" ", "%20").replace("&", "%26").replace("-", "%2D")
			election_date = datetime.strptime(user.date_of_election,'%Y-%m-%d %H:%M:%S')

			url = "https://tools.wmflabs.org/afdstats/afdstats.py?name={0}&max=&startdate={1.year}{1.month}{1.day}&altname=".format(username, election_date)

			r = requests.get(url)
			data = r.text
			soup = BeautifulSoup(data, "lxml")
			lis = soup.find_all("li")

			votes = []

			for li in lis:
				text = li.text

				start = text.find(": ")
				end = text.find(" (")
				num = text[start + len(": "):end]

				votes.append(num)
			try:
				user.keep_votes = votes[0]
				user.delete_votes = votes[1]
				user.sp_keep_votes = votes[2]
				user.sp_delete_votes = votes[3]
				user.merge_votes = votes[4]
				user.redirect_votes = votes[5]
				user.transwiki_votes = votes[6]
				user.userfy_votes = votes[7]
			except IndexError:
				5+5

			print user

add_afd_stats = AddAfDStats('../Data/10_clean.csv')
add_afd_stats.add()