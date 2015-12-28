import csv
from DataCollection.User import User

__author__ = 'lizzybradley'

class AddClasses:
	user_list = []

	def __init__(self, filename):
		with open(filename) as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:
				self.user_list.append(User(row))

	def addHasFeaturedContent(self, doPrint):
		for user in self.user_list:
			if user.featured_articles + user.featured_lists > 0:
				user.hasFeaturedContent = 1
			if doPrint:
				print user

	def addHasMoreThanOneAccount(self, doPrint):
		for user in self.user_list:
			if user.accounts > 1:
				user.hasMultipleAccounts = 1
			if doPrint:
				print user

	def addHasCategoryActivity(self):
		for user in self.user_list:
			if user.category_talk_edits + user.category_edits > 0:
				user.hasCategoryActivity = 1
			print user

add_classes = AddClasses('../../Data/16_classes.csv')

add_classes.addHasFeaturedContent(False)
add_classes.addHasMoreThanOneAccount(False)
add_classes.addHasCategoryActivity()