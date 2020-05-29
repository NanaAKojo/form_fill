from selenium import webdriver
import getpass, os

# get and set google password
ChromeDriver = os.environ['ChromeDriver']
gmail_password = getpass.getpass('Enter your gmail password: ')

# Form details
username = 'Christian Barnes'
email = 'kojobarnes338@gmail.com'
school = 'Kwame Nkrumah University of Science and Technology'
comments = ''
phonenumber = '0501595415'
address = 'Kumasi, DKC'

# forms elements
username_input = '//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input'
gender_check = '//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[1]/label/div/div[2]/div/span'
email_input = '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/input'
schcompletion = '//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input'
address_input = '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/textarea'
phone_input ='//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/input'
comments = '//*[@id="mG61Hd"]/div/div/div[2]/div[5]/div/div[2]/div[1]/div[2]/textarea'
submit = '//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div[2]/span/span'
form_next = '//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div/span'

# google  authentication
sign_in = '/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span'
google_email = '//*[@id="identifierId"]'
google_password = '//*[@id="password"]/div[1]/div/div[1]/input'
google_next = '//*[@id="identifierNext"]/span/span'
pass_next ='//*[@id="passwordNext"]/span/span'

# Open form link
driver = webdriver.Chrome(ChromeDriver)
driver.get("https://docs.google.com/forms/d/1_XyTRmCotkVFmU_V83Mma9uGUMY460CDFEe64-QgYM0/viewform?edit_requested=true")

# Google Sign in
driver.implicitly_wait(20) # wait for sometime due to network issues
driver.find_element_by_xpath(sign_in).click()
driver.implicitly_wait(20)
driver.find_element_by_xpath(google_email).send_keys('Christian.kojobarnes@gmail.com')
driver.find_element_by_xpath(google_next).click()
driver.implicitly_wait(20)
driver.find_element_by_xpath(google_password).send_keys(gmail_password)
driver.find_element_by_xpath(pass_next).click()
driver.implicitly_wait(20)

# fill form details
driver.find_element_by_xpath(username_input).send_keys(username)
driver.find_element_by_xpath(gender_check).click()
driver.find_element_by_xpath(email_input).send_keys(email)
driver.find_element_by_xpath(form_next).click()
driver.implicitly_wait(20)

driver.find_element_by_xpath(schcompletion).send_keys(school)
driver.find_element_by_xpath(address_input).send_keys(address)
driver.find_element_by_xpath(phone_input).send_keys(phonenumber)
driver.find_element_by_xpath(submit).click()

# close connection
driver.close()