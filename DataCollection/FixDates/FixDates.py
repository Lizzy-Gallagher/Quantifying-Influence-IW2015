import csv
from datetime import datetime

class FixDates:
	def fix_dates(self):
		f_wiki = open('wiki-Rfa.txt', 'r')
		votes = f_wiki.read().split("SRC:")

		with open('fixup.csv') as csvfile:
			reader = csv.DictReader(csvfile)
			i = 0
			for row in reader:
				i += 1
				if i < 131:
					continue

				foundIt = False

				for vote in votes[1:]:
					start_tgt = vote.find("TGT:")
					end_tgt = vote.find("\nVOT:")
					tgt = vote[start_tgt + len("TGT:"):end_tgt]

					start_date = vote.find("DAT:")
					end_date = vote.find("\nTXT:")
					date = vote[start_date + len("DAT:"): end_date]

					try:
						self.date_time = datetime.strptime(date, '%H:%M, %d %B %Y')
					except ValueError:
						try:
							self.date_time = datetime.strptime(date, '%H:%M, %d %b %Y')
						except ValueError:
							continue

					if ((tgt == row['username']) & (len(date) > 5)):
						foundIt = True
						print(row['username'] + ',' + str(self.date_time) + ',' + row['isSuccessful'] + ','
							  + row['votes'] + ',' + row['edit_count'] + ',' + row['year_joined'])
						break

				if not foundIt:
					print(row['username'] + ',' + '-' + ',' + row['isSuccessful'] + ','
						  + row['votes'] + ',' + row['edit_count'] + ',' + row['year_joined'])
fd = FixDates()
fd.fix_dates()

