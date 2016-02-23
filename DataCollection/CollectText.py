import csv
from DataCollection.User import User

usernames = {}

with open('../Data/19_frequency.csv') as csvfile:
	reader = csv.DictReader(csvfile)

	for row in reader:
		user = User(row)
		usernames[user.username] = 1

print len(usernames)

import random

# __author__ = 'lizzybradley'
#
# f_wiki = open('../Data/wiki-Rfa.txt', 'r')
# votes = f_wiki.read().split("SRC:")
#
# elections = {}
#
# for vote in votes[:]:
# 	start_tgt = vote.find("TGT:")
# 	end_tgt = vote.find("\nVOT:")
# 	tgt = vote[start_tgt + len("TGT:"):end_tgt]
#
# 	start_date = vote.find("DAT:")
# 	end_date = vote.find("\nTXT:")
# 	date = vote[start_date + len("DAT:"): end_date]
#
# 	start_text = vote.find("TXT:")
# 	text = vote[start_text + len("TXT:"):]
#
# 	elections[tgt.strip()] = 1
#
# 	# print text
# 	# with open("Text.txt", "a") as text_file:
# 	# 	if len(text.split(' ')) > 10 and random.randint(0,10) < 1:
# 	# 		text_file.write(text.strip())
# 	# 		print text.strip()
#
# print len(elections)
#
# f_wiki.close()



