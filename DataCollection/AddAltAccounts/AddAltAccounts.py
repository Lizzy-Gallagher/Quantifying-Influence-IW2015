import csv
import requests

from bs4 import BeautifulSoup
from DataCollection.User import User
from datetime import datetime

__author__ = 'lizzybradley'


class AddAltAccounts:
	user_list = []

	def __init__(self, filename):
		with open(filename) as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:
				self.user_list.append(User(row))

	def add(self):
		i = 2700
		for user in self.user_list[2700:2800]:
			print i
			i += 1
			username = user.username
			date_of_election = datetime.strptime(user.date_of_election, '%Y-%m-%d %H:%M:%S')

			url = "https://tools.wmflabs.org/quentinv57-tools/tools/sulinfo.php?username=" + username

			r = requests.get(url)
			data = r.text
			soup = BeautifulSoup(data, "lxml")
			trs = soup.find_all("tr")

			num_accounts = 0

			for tr in trs[1:]:
				if len(tr.find_all('td')) == 0:
					continue

				if len(tr.find_all('td')[2].text) == 0:
					continue

				month = tr.find_all('td')[2].text.split(' ')[1]
				year = tr.find_all('td')[2].text.split(' ')[2]

				cutoff_date = datetime.strptime(month + ' ' + year, '%B %Y')

				if cutoff_date < date_of_election:
					num_accounts += 1

			with open('data.csv', 'a') as file_:
				file_.write(str(user) + ',' + str(num_accounts))
				file_.write('\n')

			# print str(user) + ',' + str(num_accounts)


add_alt_accounts = AddAltAccounts('../../Data/12_total_afd.csv')
add_alt_accounts.add()
