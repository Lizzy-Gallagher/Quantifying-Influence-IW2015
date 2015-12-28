import csv
from DataCollection.User import User

__author__ = 'lizzybradley'

class AddAfDTotals:
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
			user.total_afd_votes = user.keep_votes + user.delete_votes + user.merge_votes + \
				user.redirect_votes + user.sp_delete_votes + user.sp_keep_votes + \
				user.userfy_votes + user.transwiki_votes
			print user

add_afd_totals = AddAfDTotals('../../Data/11_recover.csv')
add_afd_totals.add()
