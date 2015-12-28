__author__ = 'lizzybradley'

class User:
	username = ""
	date_of_election = ""
	isSuccessful = 0
	votes = 0
	pages_created = 0
	total_edits = 0
	article_edits = 0
	# article_talk_edits = 0
	user_edits = 0
	user_talk_edits = 0
	file_edits = 0
	file_talk_edits = 0
	template_edits = 0
	template_talk_edits = 0
	wikipedia_edits = 0
	wikipedia_talk_edits = 0
	# mediaWiki_edits = 0
	# mediaWiki_talk_edits = 0
	category_edits = 0
	category_talk_edits = 0
	draft_edits = 0
	draft_talk_edits = 0
	talk_edits = 0

	gender = 'unknown'

	days_active = 0

	keep_votes = 0
	delete_votes = 0
	sp_keep_votes = 0
	sp_delete_votes = 0
	merge_votes = 0
	redirect_votes = 0
	transwiki_votes = 0
	userfy_votes = 0

	total_afd_votes = 0

	accounts = 0

	featured_lists = 0
	featured_articles = 0

	elections = 0

	hasFeaturedContent = 0
	hasMultipleAccounts = 0
	hasCategoryActivity = 0

	images_uploaded = 0

	def __init__(self, row):
		self.username             = row['username']
		self.date_of_election     = row['date_of_election']
		self.isSuccessful         = int(row['isSuccessful'])
		self.votes                = int(row['votes'])
		self.pages_created        = int(row['pages_created'])
		self.total_edits          = int(row['total_edits'])
		self.article_edits        = int(row['article_edits'])
		# self.article_talk_edits   = int(row['article_talk_edits'])
		self.user_edits           = int(row['user_edits'])
		self.user_talk_edits      = int(row['user_talk_edits'])
		self.file_edits           = int(row['file_edits'])
		self.file_talk_edits      = int(row['file_talk_edits'])
		self.template_edits       = int(row['template_edits'])
		self.template_talk_edits  = int(row['template_talk_edits'])
		self.wikipedia_edits      = int(row['wikipedia_edits'])
		self.wikipedia_talk_edits = int(row['wikipedia_talk_edits'])
		# self.mediaWiki_edits      = int(row['mediaWiki_edits'])
		# self.mediaWiki_talk_edits = int(row['mediaWiki_talk_edits'])
		self.category_edits       = int(row['category_edits'])
		self.category_talk_edits  = int(row['category_talk_edits'])
		self.draft_edits          = int(row['draft_edits'])
		self.draft_talk_edits     = int(row['draft_talk_edits'])
		self.talk_edits           = int(row['talk_edits'])

		# Metadata
		self.gender               = row['gender']

		# Add Days Active
		self.days_active          = int(row['days_active'])

		# AfD
		self.keep_votes           = int(row['keep_votes'])
		self.delete_votes         = int(row['delete_votes'])
		self.sp_keep_votes        = int(row['sp_keep_votes'])
		self.sp_delete_votes      = int(row['sp_delete_votes'])
		self.merge_votes          = int(row['merge_votes'])
		self.redirect_votes       = int(row['redirect_votes'])
		self.transwiki_votes      = int(row['transwiki_votes'])
		self.userfy_votes         = int(row['userfy_votes'])

		self.total_afd_votes      = int(row['total_afd_votes'])

		self.accounts             = int(row['accounts'])

		self.featured_lists       = int(row['featured_lists'])
		self.featured_articles    = int(row['featured_articles'])

		self.elections            = int(row['elections'])

		self.hasFeaturedContent   = int(row['hasFeaturedContent'])
		self.hasMultipleAccounts  = int(row['hasMultipleAccounts'])
		self.hasCategoryActivity  = int(row['hasCategoryActivity'])

		self.images_uploaded      = int(row['images_uploaded'])

	def __str__(self):
		return self.username + ',' + self.date_of_election + ',' + str(self.isSuccessful) + ',' + str(self.votes) + ',' + \
			str(self.pages_created) + ',' + str(self.total_edits) + ',' + \
			str(self.article_edits) + ',' + str(self.user_edits) + ',' + \
			str(self.user_talk_edits) + ',' + str(self.file_edits) + ',' + str(self.file_talk_edits) + ',' + \
			str(self.template_edits) + ',' + str(self.template_talk_edits) + ',' + str(self.wikipedia_edits) + ',' + \
			str(self.wikipedia_talk_edits) + ',' + \
			str(self.category_edits) + ',' + str(self.category_talk_edits) + ',' + str(self.draft_edits) + ',' + \
			str(self.draft_talk_edits) + ',' + str(self.talk_edits) + ',' + self.gender + ',' + \
			str(self.days_active) + ',' + \
			str(self.keep_votes) + ',' + str(self.delete_votes) + ',' + str(self.sp_keep_votes) + ',' + \
			str(self.sp_delete_votes) + ',' + str(self.merge_votes) + ',' + str(self.redirect_votes) + ',' + \
			str(self.transwiki_votes) + ',' + str(self.userfy_votes) + ',' + \
			str(self.total_afd_votes) + ',' + str(self.accounts) + ',' + str(self.featured_lists) + ',' + \
			str(self.featured_articles) + ',' + str(self.elections) + ',' + str(self.hasFeaturedContent) + ',' + \
			str(self.hasMultipleAccounts) + ',' + str(self.hasCategoryActivity) + ',' + str(self.images_uploaded)