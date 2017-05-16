from django.utils import timezone
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create your tests here
from .forms import SumForm



class FooTest(TestCase):

	def test_one(self):
		pass


	def test_two(self):
		browser = webdriver.Chrome()

		browser.get('http://www.yahoo.com')
		assert 'Yahoo' in browser.title

		elem = browser.find_element_by_name('p')  # Find the search box
		elem.send_keys('seleniumhq' + Keys.RETURN)

		browser.quit()

	def test_three(self):
		browser = webdriver.Chrome()
		browser.get('http://127.0.0.1:8000/sum')
		try:
			element = WebDriverWait(browser, 10). until(
				EC.presence_of_element_located((By.Name, "sum"))
			)
			x = browser.find_element_by_name('x')  # Find the search box
			x.send_keys(1)
			y = browser.find_element_by_name('y')
			y.send_keys(2)
			y.send_keys(Keys.RETURN)
			browser.implicitly_wait(5)
			print (browser.find_element_by_name('sum').get_attribute('value'))

		finally:
			assert (browser.find_element_by_name('sum').get_attribute('value') == 3)
			# browser.quit()
