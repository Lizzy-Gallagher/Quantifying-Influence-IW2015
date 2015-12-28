import csv

from DataCollection.User import User

__author__ = 'lizzybradley'

class FixTotalEdits:
	user_list = []

	def __init__(self, filename):
		with open(filename) as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:
				self.user_list.append(User(row))

	def fix(self):
		for user in self.user_list:
			total_edits = user.article_edits + user.article_talk_edits + user.user_edits + user.user_talk_edits + \
				user.file_edits + user.file_talk_edits + user.template_edits + user.template_talk_edits + \
				user.wikipedia_edits + user.wikipedia_talk_edits + user.mediaWiki_edits + user.mediaWiki_talk_edits + \
				user.category_edits + user.category_talk_edits + user.draft_edits + user.draft_talk_edits + \
				user.talk_edits

			user.total_edits = total_edits
			print user

fix_total_edits = FixTotalEdits('../Data/5_no_double_votes.csv')
fix_total_edits.fix()
