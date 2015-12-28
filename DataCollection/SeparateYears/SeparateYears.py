import csv
from DataCollection.User import User
from datetime import datetime

__author__ = 'lizzybradley'

class SeparateYears:
	user_list = []
	header = 'username,date_of_election,isSuccessful,votes,pages_created,total_edits,article_edits,user_edits,user_talk_edits,file_edits,file_talk_edits,template_edits,template_talk_edits,wikipedia_edits,wikipedia_talk_edits,category_edits,category_talk_edits,draft_edits,draft_talk_edits,talk_edits,gender,days_active,keep_votes,delete_votes,sp_keep_votes,sp_delete_votes,merge_votes,redirect_votes,transwiki_votes,userfy_votes,total_afd_votes,accounts'


	def __init__(self, filename):
		with open(filename) as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:
				self.user_list.append(User(row))

	def sep(self):
		with open('../../Data/13/2003.csv', 'a') as file_:
			file_.write(self.header + '\n')
		with open('../../Data/13/2004.csv', 'a') as file_:
			file_.write(self.header + '\n')
		with open('../../Data/13/2005.csv', 'a') as file_:
			file_.write(self.header + '\n')
		with open('../../Data/13/2006.csv', 'a') as file_:
			file_.write(self.header + '\n')
		with open('../../Data/13/2007.csv', 'a') as file_:
			file_.write(self.header + '\n')
		with open('../../Data/13/2008.csv', 'a') as file_:
			file_.write(self.header + '\n')
		with open('../../Data/13/2009.csv', 'a') as file_:
			file_.write(self.header + '\n')
		with open('../../Data/13/2010.csv', 'a') as file_:
			file_.write(self.header + '\n')
		with open('../../Data/13/2011.csv', 'a') as file_:
			file_.write(self.header + '\n')
		with open('../../Data/13/2012.csv', 'a') as file_:
			file_.write(self.header + '\n')
		with open('../../Data/13/2013.csv', 'a') as file_:
			file_.write(self.header + '\n')

		for user in self.user_list:
			year = datetime.strptime(user.date_of_election, '%Y-%m-%d %H:%M:%S').year
			if year == 2003:
				with open('../../Data/13/2003.csv', 'a') as file_:
					file_.write(str(user))
					file_.write('\n')
			elif year == 2004:
				with open('../../Data/13/2004.csv', 'a') as file_:
					file_.write(str(user))
					file_.write('\n')
			elif year == 2005:
				with open('../../Data/13/2005.csv', 'a') as file_:
					file_.write(str(user))
					file_.write('\n')
			elif year == 2006:
				with open('../../Data/13/2006.csv', 'a') as file_:
					file_.write(str(user))
					file_.write('\n')
			elif year == 2007:
				with open('../../Data/13/2007.csv', 'a') as file_:
					file_.write(str(user))
					file_.write('\n')
			elif year == 2008:
				with open('../../Data/13/2008.csv', 'a') as file_:
					file_.write(str(user))
					file_.write('\n')
			elif year == 2009:
				with open('../../Data/13/2009.csv', 'a') as file_:
					file_.write(str(user))
					file_.write('\n')
			elif year == 2010:
				with open('../../Data/13/2010.csv', 'a') as file_:
					file_.write(str(user))
					file_.write('\n')
			elif year == 2011:
				with open('../../Data/13/2011.csv', 'a') as file_:
					file_.write(str(user))
					file_.write('\n')
			elif year == 2012:
				with open('../../Data/13/2012.csv', 'a') as file_:
					file_.write(str(user))
					file_.write('\n')
			elif year == 2013:
				with open('../../Data/13/2013.csv', 'a') as file_:
					file_.write(str(user))
					file_.write('\n')

separate_years = SeparateYears('../../Data/13_accounts.csv')
separate_years.sep()