import csv

__author__ = 'lizzybradley'

not_present = []
is_double = []

rows = []

with open("../Data/3_votes.csv") as data_w_votes:
	votes_reader = csv.DictReader(data_w_votes)
	# i = 1
	for row in votes_reader:
		username = row['username']
		date = row['date_of_election']

		present = False
		double = False

		with open("../Data/4_xtools.csv") as data_w_edits:
			edits_reader = csv.DictReader(data_w_edits)
			for r in edits_reader:
				username2 = r['username']
				date2 = r['date_of_election']

				if ((username == username2) & (date == date2)):
					if present:
						double = True
					else:
						present = True
						rows.append(row['username'] + ',' + row['date_of_election'] + ','  + row['isSuccessful'] + ',' + \
									row['votes'] + ',' + row['edit_count'] + ',' + row['year_joined'] + ',' + \
									row['pages_created'] + ',' + r['total_edits'] + ',' + r['article_edits'] + ',' + \
									r['article_talk_edits'] + ',' + r['user_edits'] + ',' + r['user_talk_edits'] + \
									',' + r['file_edits'] + ',' + r['file_talk_edits'] + ',' + r['template_edits'] + \
									',' + r['template_talk_edits'] + ',' + r['wikipedia_edits'] + ',' + \
									r['wikipedia_talk_edits'] + ',' + r['mediaWiki_edits'] + ',' + \
									r['mediaWiki_talk_edits'] + ',' + r['category_edits'] + ',' + r['category_talk_edits'] + \
									',' + r['draft_edits'] + ',' + r['draft_talk_edits'] + ',' + r['talk_edits'])


		# if double:
		# 	print "Double " + str(i)
		# 	is_double.append(i)
		#
		# if not present:
		# 	print "Not Present " + str(i)
		# 	not_present.append(i)
		# else:
		# 	print "Present " + str(i)

		# i += 1

# print "Not Present"
# print not_present
#
# print "Is Double"
# print is_double

for r in rows:
	print r
	# print r['username'] + ',' + r['date_of_election'] + ','  + r['isSuccessful'] + ',' + \
	# 	 r['votes'] + ',' + r['edit_count'] + ',' + r['year_joined'] + ',' + r['pages_created'] + \
	# 	',' + r['total_edits'] + ',' + r['article_edits'] + ',' + r['article_talk_edits'] + ',' + \
	# 	 r['user_edits'] + ',' + r['user_talk_edits'] + ',' + r['file_edits'] + ',' + r['file_talk_edits'] + \
	# 	',' + r['template_edits'] + ',' + r['template_talk_edits'] + ',' + r['wikipedia_edits'] + \
	# 	',' + r['wikipedia_talk_edits'] + ',' + r['mediaWiki_edits'] + ',' + r['mediaWiki_talk_edits'] + \
	# 	',' + r['category_edits'] + ',' + r['category_talk_edits'] + ',' + r['draft_edits'] + ',' + \
	# 	 r['draft_talk_edits'] + ',' + r['talk_edits']