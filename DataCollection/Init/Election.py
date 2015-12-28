from datetime import datetime

__author__ = 'lizzybradley'


class Election:
	_total_votes = 0
	_yeas = 0
	_nays = 0
	date_of_first_vote = datetime.today()

	candidate_username = ""
	is_successful = -1

	def __init__(self, date, candidate, is_successful):
		self.date_of_first_vote = date
		self.candidate_username = candidate
		self.is_successful = is_successful

	def vote_yea(self, date):
		self._total_votes += 1
		self._yeas += 1
		if date < self.date_of_first_vote:
			self._date_of_first_vote = date

	def vote_neutral(self, date):
		self._total_votes += 1
		if date < self.date_of_first_vote:
			self.date_of_first_vote = date

	def vote_nay(self, date):
		self._total_votes += 1
		self._nays += 1
		if date < self.date_of_first_vote:
			self.date_of_first_vote = date

	def ratio(self):
		return float(self._yeas) / self._total_votes
