import csv
from datetime import datetime
import requests
from DataCollection.User import User

__author__ = 'lizzybradley'

class AddImageUploaded:
	user_list = []

	def __init__(self, csv_filename):
		self.csv_filename = csv_filename
		self.filename = csv_filename[:-4]

		with open(csv_filename) as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:
				user = User(row)
				self.user_list.append(user)

	def addImagesUploaded(self):
		for user in self.user_list[:]:
			username = user.username
			date_of_election = datetime.strptime(user.date_of_election, '%Y-%m-%d %H:%M:%S')
			stop_date = date_of_election.isoformat('T') + 'Z'
			start_date = datetime.min.isoformat('T') + 'Z'
			paging = True

			total = 0
			while paging:
				url = "https://en.wikipedia.org/w/api.php?action=query&list=allimages&ailimit=500&format=json" + \
					  "&aiprop=user|timestamp&aisort=timestamp&aistart=" + start_date + "&aiend=" + stop_date + "&aiuser=" + username
				r = requests.get(url.replace(' ', '%20'))

				try:
					allimages_len = len(r.json()['query']['allimages'])
					start_date = r.json()['query']['allimages'][allimages_len-1]['timestamp']

					if allimages_len < 500:
						paging = False

					total += allimages_len
				except:
					paging = False


			user.images_uploaded = total
			print user

add_image_uploaded = AddImageUploaded('../../Data/16_classes.csv')
add_image_uploaded.addImagesUploaded()