from selenium import webdriver

# create a new Chrome browser instance
browser = webdriver.Chrome()

# navigate to the web application URL
browser.get("https://dummyDashboard.com")

# find the login input fields and enter username and password
username_input = browser.find_element_by_id("username")
password_input = browser.find_element_by_id("password")
username_input.send_keys("myusername")
password_input.send_keys("mypassword")

# find and click the login button
login_button = browser.find_element_by_id("login-button")
login_button.click()

# wait for the dashboard page to load
dashboard_title = browser.find_element_by_xpath("//h1[contains(text(), 'Dashboard')]")
assert dashboard_title.is_displayed()

# perform some actions on the dashboard page, e.g. create a new widget
new_widget_button = browser.find_element_by_xpath("//button[contains(text(), 'New Widget')]")
new_widget_button.click()

# wait for the new widget form to load and fill it out
widget_name_input = browser.find_element_by_id("widget-name")
widget_name_input.send_keys("My Widget")
widget_type_select = browser.find_element_by_id("widget-type")
widget_type_select.select_by_visible_text("Bar Chart")
create_widget_button = browser.find_element_by_xpath("//button[contains(text(), 'Create Widget')]")
create_widget_button.click()

# wait for the new widget to be created and verify it appears on the dashboard
new_widget = browser.find_element_by_xpath("//div[contains(text(), 'My Widget')]")
assert new_widget.is_displayed()

# perform logout
logout_button = browser.find_element_by_xpath("//button[contains(text(), 'Logout')]")
logout_button.click()

# wait for the login page to load
login_title = browser.find_element_by_xpath("//h1[contains(text(), 'Login')]")
assert login_title.is_displayed()

# close the browser window
browser.quit()
