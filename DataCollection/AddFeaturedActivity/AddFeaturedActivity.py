import csv
from bs4 import BeautifulSoup
import requests
import sys
from DataCollection.User import User
from datetime import datetime

__author__ = 'lizzybradley'

class AddFeaturedActivity:
	featured_lists    = {} # date - list of usernames
	featured_articles = {}

	fl_by_user = {}
	fa_by_user = {}

	user_list = []

	def pad_month(self, month):
		if month < 10:
			return "0" + str(month)
		else:
			return str(month)

	def collect(self, type, stop_year):
		featured_dict = {}

		year_num = 2015
		while year_num > stop_year:
			url = "https://en.wikipedia.org/wiki/Wikipedia:"+type+"_promoted_in_" + str(year_num)
			r = requests.get(url)
			data = r.text
			soup = BeautifulSoup(data, "lxml")
			wikitables = soup.find_all("table", {"class": "wikitable"})

			month_num = 12
			for month in wikitables:
				users = []

				anchors = month.find_all("a", href=True)
				for a in anchors:
					href = a['href']

					if href.startswith('/wiki/User:'):
						username = href[len('/wiki/User:'):]
						users.append(username)

				timestamp = str(year_num) + ':' + self.pad_month(month_num)
				featured_dict[timestamp] = users

				month_num -= 1
			year_num -= 1

		return featured_dict

	def __init__(self):
		self.featured_lists = self.collect("Featured_lists", 2004)
		self.featured_articles = self.collect("Featured_articles", 2002)

		for timestamp, users in self.featured_lists.items():
			for username in users:
				if username in self.fl_by_user:
					self.fl_by_user[username].append(timestamp)
				else:
					self.fl_by_user[username] = [timestamp]

		for timestamp, users in self.featured_articles.items():
			for username in users:
				if username in self.fa_by_user:
					self.fa_by_user[username].append(timestamp)
				else:
					self.fa_by_user[username] = [timestamp]

		print len(self.fl_by_user)
		print len(self.fa_by_user)

	def add(self, filename):
		with open(filename) as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:
				self.user_list.append(User(row))

		for user in self.user_list:
			username = user.username
			date_of_election = datetime.strptime(user.date_of_election, '%Y-%m-%d %H:%M:%S')

			if username in self.fl_by_user:
				for date in self.fl_by_user[username]:
					fl_date = datetime.strptime(date, '%Y:%m')
					if fl_date < date_of_election:
						user.featured_lists += 1
			if username in self.fa_by_user:
				for date in self.fa_by_user[username]:
					fa_date = datetime.strptime(date, '%Y:%m')
					if fa_date < date_of_election:
						user.featured_articles += 1

			print(user)

featured_activity = AddFeaturedActivity()
featured_activity.add('../../Data/13_accounts.csv')