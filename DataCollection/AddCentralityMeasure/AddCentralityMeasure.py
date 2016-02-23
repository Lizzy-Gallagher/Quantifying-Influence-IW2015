import csv
import time
import requests

from Queue import PriorityQueue
from datetime import datetime
from selenium import webdriver
import sys
from DataCollection.User import User

__author__ = 'lizzybradley'

class AddCentralityMeasure:
	user_list = []

	def __init__(self, csv_filename):
		self.csv_filename = csv_filename
		self.filename = csv_filename[:-4]

		with open(csv_filename) as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:
				user = User(row)
				self.user_list.append(user)

	def add_centrality(self):
		i = 0
		for user in self.user_list[:10]:
			print i
			i += 1

			username = user.username
			election_date = datetime.strptime(user.election_date, '%Y-%m-%d %H:%M:%S')

			self.calculate_centrality(username, election_date)

	def calculate_centrality(self, username, election_date):
		stop_date = election_date.isoformat('T') + 'Z'
		is_paging = True

		visits = {}

		url = "https://en.wikipedia.org/w/api.php?action=query&list=usercontribs&uclimit=500&format=json" + \
			  "&ucshow=minor&ucprop=title|timestamp&ucdir=newer" + \
			  "&ucuser=" + username + "&ucend=" + stop_date
		url = url.replace(' ', '+')

		while is_paging:
			r = requests.get(url)
			try:
				for contrib in r.json()['query']['usercontribs']:
					contrib_timestamp = datetime.strptime(contrib['timestamp'], '%Y-%m-%dT%H:%M:%SZ')
					if contrib_timestamp < election_date:
						title = contrib['title']
						if title in visits.keys():
							visits[title] -= 1
						else:
							visits[title] = 1
					else:
						is_paging = False

				uccontinue = r.json()['continue']['uccontinue']
				url = "https://en.wikipedia.org/w/api.php?action=query&list=usercontribs&uclimit=500&format=json" + \
					  "&ucprop=title|timestamp&ucdir=newer" + \
					  "&ucuser=" + username + "&ucend=" + stop_date + "&uccontinue=" + uccontinue
			except:
				is_paging = False

		pq = PriorityQueue()

		for visit in visits.iteritems():
			title, count = visit
			pq.put((count,title))

		top_twenty_most_edited = []
		for j in range(0,20):
			top_twenty_most_edited.append(pq.get(pq)) # Most visited article

		rank = 0
		for article_name in top_twenty_most_edited:
			print '\t ' + str(rank)
			degree = self.calculate_degree(username, election_date, article_name, rank)
			time.sleep(20)
			rank += 1

	def calculate_degree(self, username, election_date, article_name, rank):
		total_edits, fraction_of_edits_by_top_ten_percent, unique_editors = self.get_stats(article_name, election_date)

		print total_edits
		print fraction_of_edits_by_top_ten_percent
		print unique_editors

		print_string =  ','.join([str(username), str(article_name[1]), str(rank), str(total_edits), str(fraction_of_edits_by_top_ten_percent), str(unique_editors)])

		# Save for now
		with open('data.csv', 'a') as file_:
			file_.write(print_string)
			file_.write('\n')

	def get_stats(self, article_name, election_date):
		url = "https://tools.wmflabs.org/xtools-articleinfo/?article=" + article_name + "&project=en.wikipedia.org"

		driver = webdriver.PhantomJS()
		driver.set_window_size(1120, 550)
		driver.get(url)

		driver.save_screenshot('screenshot.png')

		try:
			trs = driver.find_element_by_id('monthcounts').find_elements_by_css_selector('tr')

			election_month = election_date.month
			election_year = election_date.year

			total_edits = 0
			for tr in trs[1:]:
				tds = tr.find_elements_by_css_selector('td')
				try:
					date = str(tds[0].get_attribute('innerHTML'))
					year = int(date.split(' ')[0])
					month = int(date.split(' ')[2])

					if (year < election_year) or ((year == election_year) and month <= election_month):
						total_edits += int(tds[1].get_attribute('innerHTML'))
					else:
						break
				except:
					continue

			text = driver.find_elements_by_css_selector('.table-condensed tr:last-child td:last-child')[0].get_attribute(
				'innerHTML')
			fraction_of_edits_by_top_ten_percent = float(text.split("(")[1][:-2]) * .01
			unique_editors = int(
				driver.find_elements_by_css_selector('.table-condensed tr:nth-child(5) td:last-child')[0].get_attribute(
					'innerHTML'))

			driver.quit()

			return total_edits, fraction_of_edits_by_top_ten_percent, unique_editors

		except:
			print '\t Failed, waiting 10 minutes'
			time.sleep(600)
			driver.quit()
			return '-', '-', '-'

add_centrality_measure = AddCentralityMeasure('../../Data/18_edits_alt.csv')
add_centrality_measure.add_centrality()