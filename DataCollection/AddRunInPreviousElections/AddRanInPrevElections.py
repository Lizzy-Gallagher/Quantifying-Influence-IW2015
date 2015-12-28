import csv
from datetime import datetime
from DataCollection.AddRunInPreviousElections.Election import Election

from DataCollection.User import User

__author__ = 'lizzybradley'

f = open('../../Data/wiki-Rfa.txt', 'r')
votes = f.read().split("SRC:")

elections = []

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

	date_time = None
	if len(date) != 0:
		try:
			date_time = datetime.strptime(date, '%H:%M, %d %B %Y')
		except ValueError:
			try:
				date_time = datetime.strptime(date, '%H:%M, %d %b %Y')
			except ValueError:
				print date

	if date_time is None:
		continue

	if len(elections) == 0:
		election = Election(date_time, tgt)
		elections.append(election)

	election = elections[len(elections) - 1]

	# New election
	if election.candidate_username != tgt:
		election = Election(date_time, tgt)
		elections.append(election)

elections_by_user = {}

for election in elections:
	username = election.candidate_username

	if username in elections_by_user:
		elections_by_user[username] += 1
	else:
		elections_by_user[username] = 1

print elections_by_user

user_list = []
with open('../../Data/14_fa_fl.csv') as csvfile:
	reader = csv.DictReader(csvfile)

	for row in reader:
		user_list.append(User(row))

for user in user_list:
	try:
		user.elections = elections_by_user[user.username]
		print user
	except:
		user.elections = 1
		print user