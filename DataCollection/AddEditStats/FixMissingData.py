import csv
from DataCollection.User import User

__author__ = 'lizzybradley'

user_list_18 = []

csv_filename = '../../Data/18_edits.csv'
with open(csv_filename) as csvfile:
	reader = csv.DictReader(csvfile)

	for row in reader:
		user = User(row)
		user_list_18.append(user)

user_list_17 = []

csv_filename = '../../Data/17_images.csv'
with open(csv_filename) as csvfile:
	reader = csv.DictReader(csvfile)

	for row in reader:
		user = User(row)
		user_list_17.append(user)

i = 0
for user in user_list_17:
	username_17 = user.username
	present = False

	for user_18 in user_list_18:
		if user_18.username == username_17:
			present = True

	if not present:
		print i

	i += 1
