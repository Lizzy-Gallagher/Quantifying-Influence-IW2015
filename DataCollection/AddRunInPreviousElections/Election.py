__author__ = 'lizzybradley'

class Election:
	date_of_first_vote = None
	candidate_username = ""

	def __init__(self, date, candidate):
		self.date_of_first_vote = date
		self.candidate_username = candidate