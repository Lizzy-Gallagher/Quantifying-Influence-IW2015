import csv
from datetime import datetime
from selenium import webdriver

from UserEdits import UserEdits

__author__ = 'lizzybradley'

html = "https://en.wikipedia.org/w/index.php?limit=5000&" \
	   "title=Special%3AContributions&contribs=user&target={0}&namespace=" \
	   "&tagfilter=&year={1}&month={2}"

class AddCorrectEditCounts:
	def __init__(self, data_file):
		self.data_file = data_file

	def get_attribute(self, name_of_attribute, string):
		start = string.find(name_of_attribute + ":")
		if start != -1:
			offset = start + len(name_of_attribute + ":")
			end = offset + string[offset:].find(" edits")
			article = string[offset:end]
			return int(article)
		else:
			return 0

	def get_edit_counts(self, username, election_month, election_year, row):
		url = "https://tools.wmflabs.org/xtools/pcount/?user=" + username + "&project=en.wikipedia.org"

		driver = webdriver.PhantomJS()
		driver.set_window_size(1120, 550)
		driver.get(url)

		user_edits = UserEdits()

		try:
			tds = driver.find_element_by_id('monthcounts').find_elements_by_css_selector('td')
		except:
			print 'Failed on: ' + username
			return user_edits

		for td in tds:
			title = td.get_attribute('title')

			if len(title) > 0:
				year = int(title[:4])
				month = int(title[4:6])

				if int(year) <= int(election_year) and int(month) <= int(election_month):
					user_edits.article += self.get_attribute("Article", title)
					user_edits.article_talk += self.get_attribute("Article talk", title)
					user_edits.user += self.get_attribute("User", title)
					user_edits.user_talk += self.get_attribute("User talk", title)
					user_edits.file += self.get_attribute("File", title)
					user_edits.file_talk += self.get_attribute("File talk", title)
					user_edits.template += self.get_attribute("Template", title)
					user_edits.template_talk += self.get_attribute("Template talk", title)
					user_edits.wikipedia += self.get_attribute("Wikipedia", title)
					user_edits.wikipedia_talk += self.get_attribute("Wikipedia talk", title)
					user_edits.mediaWiki += self.get_attribute("Mediawiki", title)
					user_edits.mediaWiki_talk += self.get_attribute("Mediawiki talk", title)
					user_edits.category += self.get_attribute("Category", title)
					user_edits.category_talk += self.get_attribute("Category talk", title)
					user_edits.draft += self.get_attribute("Draft", title)
					user_edits.draft_talk += self.get_attribute("Draft talk", title)
					user_edits.talk += self.get_attribute("Talk", title)

					user_edits.total_edits += user_edits.article + user_edits.article_talk + user_edits.user + \
											  user_edits.user_talk + user_edits.file + user_edits.file_talk + \
											  user_edits.template + user_edits.template_talk + \
											  user_edits.wikipedia + user_edits.wikipedia_talk + \
											  user_edits.mediaWiki + user_edits.mediaWiki_talk + \
											  user_edits.category + user_edits.category_talk + user_edits.draft + \
											  user_edits.draft_talk + user_edits.talk
		driver.quit()

		print row['username'] + ',' + \
			  row['date_of_election'] + ',' + \
			  row['isSuccessful'] + ',' + \
			  row['votes'] + ',' + \
			  row['edit_count'] + ',' + \
			  row['year_joined'] + ',' + \
			  row['pages_created'] + ',' + \
			  str(user_edits.total_edits) + ',' + \
			  str(user_edits.article) + ',' + \
			  str(user_edits.article_talk) + ',' + \
			  str(user_edits.user) + ',' + \
			  str(user_edits.user_talk) + ',' + \
			  str(user_edits.file) + ',' + \
			  str(user_edits.file_talk) + ',' + \
			  str(user_edits.template) + ',' + \
			  str(user_edits.template_talk) + ',' + \
			  str(user_edits.wikipedia) + ',' + \
			  str(user_edits.wikipedia_talk) + ',' + \
			  str(user_edits.mediaWiki) + ',' + \
			  str(user_edits.mediaWiki_talk) + ',' + \
			  str(user_edits.category) + ',' + \
			  str(user_edits.category_talk) + ',' + \
			  str(user_edits.draft) + ',' + \
			  str(user_edits.draft_talk) + ',' + \
			  str(user_edits.talk)

	def generate_correct_edit_counts(self):
		with open(self.data_file) as csvfile:
			reader = csv.DictReader(csvfile)

			rows = []

			for row in reader:
				rows.append(row)

			start = 687
			end   = 701
			# for row1, row2 in zip(rows, rows):
			for row1 in rows[start:end]:
				curr_rows = []
				curr_rows.append(row1)
				# curr_rows.append(row2)

				usernames = []
				years = []
				months = []

				t = []

				for row in curr_rows:
					usernames.append(row['username'])

					election_date = row['date_of_election']
					election_date = datetime.strptime(election_date.lstrip(), "%Y-%m-%d %H:%M:%S")

					years.append(election_date.year)
					months.append(election_date.month)

				self.get_edit_counts(usernames[0], months[0], years[0], curr_rows[0])

				# for i in range(len(curr_rows)):
				# 	t.append(Thread(target=self.get_edit_counts, args=[usernames[i], months[i], years[i], curr_rows[i], i]))
				# for _ in t:
				# 	_.start()
				# for _ in t:
				# 	_.join()




