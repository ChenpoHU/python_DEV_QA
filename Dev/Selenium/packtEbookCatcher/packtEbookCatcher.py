import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user = os.environ.get('PACKT_USER')
pw = os.environ.get('PACKT_PW')

login = 'https://www.packtpub.com/login'

driver = webdriver.Safari()
driver.get(login)

driver.find_element_by_id('login-input-email').send_keys(user)
driver.find_element_by_id('login-input-password').send_keys(pw + Keys.RETURN)

driver.find_element_by_link_text('Sign In').click()

elements = driver.find_elements_by_class_name("product-line")
books = {e.get_attribute('nid'): e.get_attribute('title') for e in elements}

driver.close()

import re

DOWNLOAD_URL = 'https://www.packtpub.com/ebook_download/{nid}/{ebook_format}'
BOOK_FORMATS = 'pdf epub mobi'

def get_books(grep, ebook_format):
    grep = grep.lower()
    ebook_format = ebook_format.lower()
    if ebook_format not in BOOK_FORMATS.split():
        raise ValueError(f'Not a valid book format (valid are: {BOOK_FORMATS})')
        
    for nid, title in books.items():
        if re.search(grep, title.lower()):
            url = DOWNLOAD_URL.format(nid=nid, ebook_format=ebook_format)
            print(title, url)


get_books('python.*data', 'mobi')
