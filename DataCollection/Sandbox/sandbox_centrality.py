from selenium import webdriver

__author__ = 'lizzybradley'

article_name = "Black+Cat+%28manga%29"
url = "https://tools.wmflabs.org/xtools-articleinfo/?article=" + article_name + "&project=en.wikipedia.org"

driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
driver.get(url)

text = driver.find_elements_by_css_selector('.table-condensed tr:last-child td:last-child')[0].get_attribute('innerHTML')

fraction_of_edits_by_top_ten_percent = float(text.split("(")[1][:-2]) * .01
unique_editors = int(driver.find_elements_by_css_selector('.table-condensed tr:nth-child(5) td:last-child')[0].get_attribute('innerHTML'))

trs = driver.find_element_by_id('monthcounts').find_elements_by_css_selector('tr')

election_month = 5
election_year  = 2010

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

print total_edits

driver.quit()

