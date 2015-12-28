import csv
from DataCollection.User import User

__author__ = 'lizzybradley'

new_user_list = []
old_user_list = []

with open('../../Data/13_accounts.csv') as csvfile:
	reader = csv.DictReader(csvfile)

	for row in reader:
		new_user_list.append(row['username'] + ' ' + row['date_of_election'])

with open('../../Data/12_total_afd.csv') as csvfile:
	reader = csv.DictReader(csvfile)

	for row in reader:
		old_user_list.append(row['username'] + ' ' + row['date_of_election'])

for username in old_user_list:
	present = False

	for username2 in new_user_list:
		if username == username2:
			present = True
			break

	if not present:
		print username