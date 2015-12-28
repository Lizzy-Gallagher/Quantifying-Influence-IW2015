import csv
import logging
import traceback
from bs4 import BeautifulSoup
from datetime import datetime, time
import multiprocessing
import requests
import re

__author__ = 'lizzybradley'


class PagesCreated:

	def createNewItem(self, item):
		try:
			username = item[0]
			election_date = datetime.strptime(item[1], "%Y-%m-%d %H:%M:%S")
			pages_created = self.get_pages_created(username, election_date)
			item.append(pages_created)

			print ','.join(map(str, item))

		except Exception as e:
			print "Failed:" + str(item) + str(e)
			logging.error(traceback.format_exc())

	def append_pages_created(self, toOpen, toSave):
		v = open(toOpen)
		r = csv.reader(v)
		row0 = r.next()
		row0.append('content_pages_created')

		# items = []

		i = 0
		for item in list(r)[i:]:
			print "||||| " + str(i)
			i += 1
			# print "Started: " + str(item)
			p = multiprocessing.Process(target=self.createNewItem, name='create_new_item', args=(item,))
			p.start()

			# Wait twenty minutes to process
			p.join(1200)

			# Terminate
			if p.is_alive():
				print "Timed out: " + str(item)
				p.terminate()
				p.join()

		# with open(toSave, 'w') as toWrite:
		# 	writer = csv.writer(toWrite, delimiter=',')
		# 	writer.writerow(row0)
		# 	for item in items:
		# 		writer.writerow(item)

	def get_pages_created(self, username, election_date):
		html = "https://tools.wmflabs.org/xtools/pages/?user="
		end_html = "&lang=en&wiki=wikipedia&namespace=0&redirects=none&limit=100000"

		time1 = datetime.now()
		url = html + username + end_html
		r = requests.get(url)
		# print "Requests time:"
		# print datetime.now() - time1

		time2 = datetime.now()
		data = r.text
		soup = BeautifulSoup(data, "lxml")
		trs = soup.find_all("tr")
		# print "Soup time:"
		# print datetime.now() - time2

		try:
			last_num = trs[-1].td.string[:-1]
		except TypeError:
			return 0
		first_num = 0

		# time3 = datetime.now()
		pattern = re.compile("[0-9]+.")
		for tr in reversed(trs):
			if tr.td is not None:
				if tr.td.string is not None and pattern.match(tr.td.string):
					date = tr.contents[5].text

					date = datetime.strptime(date, "%Y-%m-%d")
					if date < election_date:
						first_num = tr.td.string[:-1]
					else:
						break
		# print "Parse time:"
		# print datetime.now() - time3


		num_pages_created = int(last_num) - int(first_num) + 1
		return num_pages_created