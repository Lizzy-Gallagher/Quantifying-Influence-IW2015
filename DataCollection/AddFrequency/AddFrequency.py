import csv
from DataCollection.User import User

__author__ = 'lizzybradley'

class AddFrequency:
	user_list = []

	def __init__(self, csv_filename):
		self.csv_filename = csv_filename
		self.filename = csv_filename[:-4]

		with open(csv_filename) as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:
				user = User(row)
				self.user_list.append(user)

	def add(self):
		for user in self.user_list:
			if user.days_active == 0:
				user.edits_per_day = user.total_edits
			else:
				edits_per_day = float(user.total_edits) / float(user.days_active)
				user.edits_per_day = edits_per_day
			print user

add_frequency = AddFrequency('../../Data/18_edits_alt.csv')
add_frequency.add()