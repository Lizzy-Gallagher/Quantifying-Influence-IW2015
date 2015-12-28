import csv
from DataCollection.User import User

__author__ = 'lizzybradley'

with open('Data/9_AfD_stats.csv') as csvfile:
	reader = csv.DictReader(csvfile)

	for row in reader:
		user = User(row)
		print user