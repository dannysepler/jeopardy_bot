# -----------------------------
#
# This was used in the initial
# iterations of the twitterbot.
# it would post in pastebin -- as 
# opposed to wordpress, which is
# does now. pastebin was uglier.
#
# I'm keeping this in the source
# code just in case
#
# -----------------------------



import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def log_into_pastebin(browser):
	browser.find_element_by_xpath('//*[@id="content_left"]/div[4]/div[2]/a[2]').click()

	browser.find_element_by_xpath('//*[@id="myform"]/div/div[1]/div[2]/input').send_keys('jeopardybot')
	browser.find_element_by_xpath('//*[@id="myform"]/div/div[2]/div[2]/input').send_keys('jeopardybotpastebin')
	browser.find_element_by_xpath('//*[@id="myform"]/div/div[3]/div[2]/input').click()

	browser.find_element_by_xpath('//*[@id="header_bottom"]/div/a[1]').click()

def post_in_pastebin(q):
	browser = webdriver.Chrome()
	browser.get('http://pastebin.com')

	log_into_pastebin(browser)

	# populate + send
	browser.find_element_by_xpath('//*[@id="paste_code"]').send_keys(
		"answer: "+str(q[6])+"\n\n"+

		"category: "+str(q[3])+"\n"+
		"question: "+str(q[5])+"\n\n"+

		"value: "+str(q[4])+"\n"+
		"air date: "+str(q[1]))

	browser.find_element_by_xpath('//*[@id="myform"]/div[3]/div[4]/div[2]/input').send_keys("Jeopardy!")
	browser.find_element_by_xpath('//*[@id="submit"]').click()

	# return link
	url = browser.find_element_by_xpath('//*[@id="content_left"]/div[1]/div[3]/div[3]/a[4]').get_attribute('href')
	browser.close()

	return url