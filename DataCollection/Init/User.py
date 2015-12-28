from datetime import datetime

__author__ = 'lizzybradley'

class User:
	date = datetime.today()

	is_voter = 0
	is_loser = 0
	is_winner = 0

	winner_count = 0
	loser_count = 0
	voter_count = 0

	def __init__(self, username, date):
		self.username = username
		self.date = date

	def voted(self):
		self.is_voter = 1
		self.voter_count += 1

	def lost(self):
		self.is_loser = 1
		self.loser_count += 1

	def won(self):
		self.is_winner = 1
		self.winner_count += 1