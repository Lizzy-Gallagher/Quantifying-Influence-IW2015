import csv
from DataCollection.User import User

__author__ = 'lizzybradley'

class ConvertToARFF:
	user_list = []
	is_class = ['isSuccessful', 'hasFeaturedContent', 'hasMultipleAccounts', 'hasCategoryActivity']

	def __init__(self, csv_filename):
		self.csv_filename = csv_filename
		self.filename = csv_filename[:-4]

		with open(csv_filename) as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:
				user = User(row)
				self.user_list.append(user)

	def convert(self):
		f = open(self.filename + '.arff','w')
		f.write('@relation ' + self.filename + '\n\n')

		for var in vars(self.user_list[0]):
			if var in self.is_class:
				f.write('@attribute ' + var + ' {1, 0}\n')
			elif var != 'username' and var != 'date_of_election' and var != 'gender':
				f.write('@attribute ' + var + ' ' + 'numeric\n')
		f.write('\n\n@data\n')

		for user in self.user_list:
			line = ""
			for value in vars(user).values():
				try:
					if value[0]:
						line = line
				except:
					line += str(value) + ' , '
			line = line[:-3]

			f.write(line + '\n')

		f.close()

filename = raw_input('Enter Filename: ')
convert_to_arff = ConvertToARFF('../Data/' + filename + '.csv')
convert_to_arff.convert()