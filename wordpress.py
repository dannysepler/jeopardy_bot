import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def post_in_wordpress(q):
	browser = webdriver.Chrome()

	# LOG IN
	browser.get('https://jeopardybot.wordpress.com/wp-login.php')
	browser.find_element_by_xpath('//*[@id="user_login"]').send_keys('jeopardybot')
	browser.find_element_by_xpath('//*[@id="user_pass"]').send_keys('jeopardy_bot')
	browser.find_element_by_xpath('//*[@id="wp-submit"]').click()

	# POST QUESTION
	browser.find_element_by_xpath('//*[@id="wp-admin-bar-ab-new-post"]/a').click()

	# TITLE
		# loops that look like this are here because wordpress
		# is slow in these steps. which crashes the program.
	while(True):
		try:
			browser.find_element_by_xpath('//*[@id="title"]').send_keys('Answer: '+str(q[6]))
			break
		except: # error
			continue

	# FULL TEXT
		# question
	while(True):
		try:
			browser.find_element_by_xpath('//*[@id="mceu_9"]/button/i').click()
			break
		except: # error
			continue
	browser.find_element_by_xpath('//*[@id="mceu_10"]/button/i').click() # italic

	browser.switch_to.frame(browser.find_element_by_tag_name('iframe'))
	iframe = browser.find_element_by_xpath('html/body')
	iframe.send_keys('Question: '+str(q[5])+'\n')

	browser.switch_to.default_content()

		# un-bold and un-italic
	browser.find_element_by_xpath('//*[@id="mceu_9"]/button/i').click() # un-bold
	browser.find_element_by_xpath('//*[@id="mceu_10"]/button/i').click() # un-italic

		# horizontal line
	browser.find_element_by_xpath('//*[@id="mceu_15"]/button').click() # horizontal line

		# question body
	browser.switch_to.frame(browser.find_element_by_tag_name('iframe'))
	iframe = browser.find_element_by_xpath('html/body')
	iframe.send_keys(
		'Category: '	+str(q[3])+'\n'+
		'Value: '		+str(q[4])+'\n'+
		'Air Date: '	+str(q[1]))

		# publish
	browser.switch_to.default_content()
	browser.find_element_by_xpath('//*[@id="publish-button"]').click()

	# get link
	while(True):
		try:
			browser.find_element_by_xpath('//*[@id="editor"]/div[1]/p/a').click()
			break
		except: # error
			continue

	# link = browser.current_url
	link = browser.find_element_by_xpath('//*[@id="editor"]/div[1]/p/a').get_attribute('href')

	browser.quit()	

	# print link
	return link