from django.utils import timezone
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Create your tests here
from .forms import SumForm



class FooTest(TestCase):

	def test_one(self):
		pass



	def test_two(self):
		
		browser = webdriver.Chrome()
		browser.get('http://127.0.0.1:8000/sum')
		x = browser.find_element_by_name('x')  # Find the search box
		x.send_keys(5)
		y = browser.find_element_by_name('y')
		y.send_keys(2)
		browser.find_element_by_name('subbut').click()
		#browser.implicitly_wait(10)
		#browser.get('http://127.0.0.1:8000/sum')
		#browser.implicitly_wait(10)
		WebDriverWait(browser, 5).until(
		    EC.text_to_be_present_in_element(
		        (By.ID, 'sum'),
		        '7'
		    )
		)



	def test_four(self):
		
		browser = webdriver.Chrome()
		browser.get('http://127.0.0.1:8000/sum')
		x = browser.find_element_by_name('x')  # Find the search box
		x.send_keys(1)
		y = browser.find_element_by_name('y')
		y.send_keys(2)
		browser.find_element_by_name('subbut').click()
		#browser.implicitly_wait(10)
		#browser.get('http://127.0.0.1:8000/sum')
		#browser.implicitly_wait(10)
		WebDriverWait(browser, 5).until(
		    EC.text_to_be_present_in_element(
		        (By.ID, 'sum'),
		        '3'
		    )
		)


	def test_three(self):
		
		browser = webdriver.Chrome()
		browser.get('http://127.0.0.1:8000/sum')
		x = browser.find_element_by_name('x')  # Find the search box
		x.send_keys("abcd")
		y = browser.find_element_by_name('y')
		y.send_keys("efgh")
		browser.find_element_by_name('subbut').click()
		#browser.implicitly_wait(10)
		#browser.get('http://127.0.0.1:8000/sum')
		#browser.implicitly_wait(10)
		WebDriverWait(browser, 5).until(
		    EC.text_to_be_present_in_element(
		        (By.ID, 'sum'),
		        "Not Valid"
		    )
		)
		
		"""
		#assert (bintsum.get_attribute('value') == None)
		# browser.quit()
		browser = Chrome()
		response = browser.request('POST', 'http://127.0.0.1:8000/sum/', data={"x": "1", "y": "2"})
		#browser.get('http://127.0.0.1:8000/sum')
		browser.implicitly_wait(5)
		#print(response)
		#intsum = browser.find_element_by_name('sum')
		#print ("INt sum value is" + intsum.get_attribute('value'))
		pass
		"""