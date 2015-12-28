import csv

__author__ = 'lizzybradley'

# with open('../Data/3_votes.csv') as csvfile:
# 	reader = csv.DictReader(csvfile)
#
# 	for row in reader:
# 		print row['username'] + ',' + \
# 			  row['date_of_election'] + ',' + \
# 			  row['isSuccessful'] + ',' + \
# 			  row['votes'] + ',' + \
# 			  row['edit_count'] + ',' + \
# 			  row['year_joined'] + ',' + \
# 			  row['pages_created']

successful = 0
unsuccessful = 0

with open('../Data/5_no_double_votes.csv') as csvfile:
	reader = csv.DictReader(csvfile)

	for row in reader:
		if row["isSuccessful"] == "1":
			successful += 1
		else:
			unsuccessful += 1

print successful
print unsuccessful

	# for row in reader:
	# 	print row['username'] + ',' + \
	# 		  row['date_of_election'] + ',' + \
	# 		  row['isSuccessful'] + ',' + \
	# 		  row['votes'] + ',' + \
	# 		  row['edit_count'] + ',' + \
	# 		  row['year_joined'] + ',' + \
	# 		  row['pages_created']