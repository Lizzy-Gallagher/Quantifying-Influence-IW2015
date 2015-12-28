import csv
from DataCollection.User import User

__author__ = 'lizzybradley'

user_list_from_9 = []
user_list_from_8 = []

with open('../Data/9_dupl.csv') as csvfile:
	reader = csv.DictReader(csvfile)

	for row in reader:
		user = User(row)
		user_list_from_9.append(user)

with open('../Data/8_days_active.csv') as csv2file:
	reader = csv.DictReader(csv2file)

	for row in reader:
		user_list_from_8.append(User(row))

# Is anyone missing
# for user in user_list_from_8:
# 	username = user.username
# 	election_date = user.date_of_election
#
# 	isIncluded = False
#
# 	for user2 in user_list_from_9:
# 		if (user2.username == username) and (user2.date_of_election == election_date):
# 			isIncluded = True
# 			break
#
# 	if not isIncluded:
# 		print "Not included: " + username

user_dict = {}

# Is anyone duplicated
for user in user_list_from_8:
	if user_dict.__contains__(user.username + user.date_of_election):
		print "Duplicate: " + user.username + ' ' + user.date_of_election
	else:
		user_dict[user.username + user.date_of_election] = 0
		# print user