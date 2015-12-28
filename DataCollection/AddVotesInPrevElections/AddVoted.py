import csv
from datetime import datetime

__author__ = 'lizzybradley'

class AddVoted:
	user_to_election_date = {}
	user_to_votes = {}

	def __init__(self, dataFile):
		self.dataFile = dataFile
		with open(dataFile) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				username = row['username']
				election_date = row['date_of_election']
				self.user_to_election_date[username] = datetime.strptime(election_date.lstrip(), "%Y-%m-%d %H:%M:%S")
				self.user_to_votes[username] = 0

	def add_voted(self):
		f_wiki = open('../Data/wiki-Rfa.txt', 'r')
		votes = f_wiki.read().split("SRC:")

		for vote in votes[1:]:
			voter = vote.split("\n")[0]

			start_tgt = vote.find("TGT:")
			end_tgt = vote.find("\nVOT:")
			tgt = vote[start_tgt + len("TGT:"):end_tgt]

			start_vote_dir = vote.find("VOT:")
			end_vote_dir = vote.find("\nRES:")
			vote_dir = vote[start_vote_dir + len("VOT:"):end_vote_dir]

			start_res = vote.find("RES:")
			end_res = vote.find("\nYEA:")
			res = int(vote[start_res + len("RES:"): end_res])

			start_date = vote.find("DAT:")
			end_date = vote.find("\nTXT:")
			date = vote[start_date + len("DAT:"): end_date]

			date_time = datetime.today()
			if len(date) != 0:
				try:
					date_time = datetime.strptime(date, '%H:%M, %d %B %Y')
				except ValueError:
					try:
						date_time = datetime.strptime(date, '%H:%M, %d %b %Y')
					except ValueError:
						continue

			if (self.user_to_election_date.has_key(voter)):
				if (self.user_to_election_date[voter] > date_time):
					self.user_to_votes[voter] = self.user_to_votes[voter] + 1

	def print_newData(self):
		with open(self.dataFile) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				username = row['username']
				row['votes'] = self.user_to_votes[username]
				print str(row['username']) +',' + str(row['date_of_election']) + ',' + \
					str(row['isSuccessful']) + ',' + str(row['votes']) + ',' + \
					str(row['edit_count']) + ',' + str(row['year_joined']) + ',' + str(row['pages_created'])