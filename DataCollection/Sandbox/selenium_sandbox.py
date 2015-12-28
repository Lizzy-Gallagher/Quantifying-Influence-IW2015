from selenium import webdriver


def gather(name_of_attribute, string):
	start = string.find(name_of_attribute + ":")
	if start != -1:
		offset = start + len(name_of_attribute + ":")
		end = offset + string[offset:].find(" edits")
		article = string[offset:end]
		return article.lstrip().rstrip()
	else:
		return 0

driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)

driver.get("https://tools.wmflabs.org/xtools/pcount/?user=BDD&project=en.wikipedia.org")

tds = driver.find_element_by_id('monthcounts').find_elements_by_css_selector('td')
for td in tds:
	title = td.get_attribute("title")

	if len(title) > 0:
		year = title[:4]
		month = title[4:6]

		article = gather("Article", title)
		article_talk = gather("Article talk", title)
		user = gather("User", title)
		user_talk = gather("User talk", title)
		file = gather("File", title)
		file_talk = gather("File talk", title)
		template = gather("Template", title)
		template_talk = gather("Template talk", title)
		wikipedia = gather("Wikipedia", title)
		wikipedia_talk = gather("Wikipedia talk", title)
		mediaWiki = gather("Mediawiki", title)
		mediaWiki_talk = gather("Mediawiki talk", title)
		category = gather("Category", title)
		category_talk = gather("Category talk", title)
		draft = gather("Draft", title)
		draft_talk = gather("Draft talk", title)
		talk = gather("Talk", title)

		print article
		print '\n'

driver.quit()