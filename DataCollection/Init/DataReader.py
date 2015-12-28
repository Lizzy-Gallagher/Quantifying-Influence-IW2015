import csv
from datetime import datetime

import requests

from DataCollection.Init.User import User
from DataCollection.Init.Election import Election

__author__ = 'lizzybradley'


def create_request(usernames):
	html = "https://en.wikipedia.org/w/api.php?action=query&list=users&" \
		   "format=json&usprop=blockinfo%7Cgroups%7Ceditcount%7Cregistration%7Cemailable%7Cgender&" \
		   "ususers="

	for username in usernames:
		html = html + username.replace(" ", "%20").replace("&", "%26") + "%7C"

	return html[:-3]

# Collect voters separately
# Cycle through elections,

class DataReader:
	voters = set
	losers = set
	winners = set
	elections = []

	def read_file(self):
		voters = []
		losers = []
		winners = []
		elections = []

		f = open('wiki-Rfa.txt', 'r')
		votes = f.read().split("SRC:")

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
						print date

			if len(elections) == 0:
				election = Election(date_time, tgt, res)
				elections.append(election)

			election = elections[len(elections) - 1]

			# New election
			if election.candidate_username != tgt:
				election = Election(date_time, tgt, res)
				elections.append(election)

			if vote_dir == -1:
				election.vote_nay(date_time)
			elif vote_dir == 0:
				election.vote_neutral(date_time)
			else:
				election.vote_yea(date_time)

			voters.append(voter)

		for election in elections:
			if election.is_successful:
				winners.append(election.candidate_username)
			else:
				losers.append(election.candidate_username)

		self.voters = voters
		self.winners = winners
		self.losers = losers
		self.elections = elections

	def save_usernames(self):
		# user_dict = {}
		users = []
		for election in self.elections:
			username = election.candidate_username
			date = election.date_of_first_vote
			user = User(username, date)
			if election.is_successful == 1:
				user.won()
			else:
				user.lost()

			# users.append(user)

		with open('1_year_joined.csv', 'w') as toWrite:
			writer = csv.writer(toWrite, delimiter=',')
			writer.writerow(['username', 'date_of_election', 'isSuccessful', 'votes', 'edit_count', 'year_joined'])

			self.iter_through_dict(writer, users)

	def iter_through_dict(self, writer, users_list):
		j = 0
		set_iter = iter(users_list)
		print len(users_list)
		for v1, v2, v3, v4, v5, v6, v7, v8, v9, v10 in zip(set_iter, set_iter, set_iter, set_iter, set_iter,
														   set_iter, set_iter, set_iter, set_iter, set_iter):
			print "Starting set " + str(j)
			j += 10
			users = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10]
			usernames = [v1.username, v2.username, v3.username, v4.username, v5.username,
						 v6.username, v7.username, v8.username, v9.username, v10.username]
			url = create_request(usernames)
			r = requests.get(url)

			for i in range(0, len(usernames)):
				try:
					edit_count = r.json()['query']['users'][i]['editcount']
					year_joined = r.json()['query']['users'][i]['registration'][:4]
					user = users[i]
					writer.writerow(
						[usernames[i], user.date, user.is_winner, user.voter_count, edit_count, year_joined])
				except KeyError:
					continue
				# print "KeyError on " + usernames[i]
				except TypeError:
					continue
				# print "TypeError on " + usernames[i]
				except IndexError:
					print(usernames[i])
					continue

	def add_pages_added(self, username):
		1
