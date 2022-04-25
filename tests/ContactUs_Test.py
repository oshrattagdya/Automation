from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def init():
    driver = webdriver.Chrome('..\drivers\chromedriver.exe')
    driver.get("https://atid.store/")
    driver.maximize_window()
    return driver

name = "oshrat"
subject = " n "
email = "oshrattagadya@gmail.com"
message = "bla bla bla"

1
def test_contact_correctly():
    driver = init()
    driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[7]/a[1]").click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#wpforms-15-field_0").send_keys(name)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#wpforms-15-field_5").send_keys(subject)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#wpforms-15-field_4").send_keys(email)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#wpforms-15-field_2").send_keys(message)
    sleep(2)
    driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()
    value = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/p[1]").get_attribute("innerText")
    assert value == "Thanks for contacting us! We will be in touch with you shortly."
    driver.quit()

test_contact_correctly()

#2
def test_when_subject_null():
    driver = init()
    driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[7]/a[1]").click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#wpforms-15-field_0").send_keys(name)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_4").send_keys(email)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_2").send_keys(message)
    sleep(2)
    driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()
    value = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/p[1]").get_attribute("innerText")
    assert value == "Thanks for contacting us! We will be in touch with you shortly."
    driver.quit()

test_when_subject_null()

#3
def test_when_email_null():
    driver = init()
    driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[7]/a[1]").click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_0").send_keys(name)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#wpforms-15-field_5").send_keys(subject)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_2").send_keys(message)
    sleep(2)
    driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()
    value = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/label[2]").get_attribute("innerText")
    assert value == "This field is required."
    driver.quit()

test_when_email_null()

#4
def test_when_message_null():
    driver = init()
    driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[7]/a[1]").click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_0").send_keys(name)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_5").send_keys(subject)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_4").send_keys(email)
    sleep(2)
    driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()
    value = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/label[2]").get_attribute("innerText")
    assert value == "This field is required."
    driver.quit()


5
def test_when_name_null():
    driver = init()
    driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[7]/a[1]").click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_5").send_keys(subject)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_4").send_keys(email)
    sleep(2)
    driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()
    value = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/label[2]").get_attribute("innerText")
    assert value == "This field is required."
    driver.quit()


# #6
def test_when_nameandsubject_null():
    driver = init()
    driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[7]/a[1]").click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_4").send_keys(email)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_2").send_keys(message)
    sleep(2)
    driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()

    namefiled = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/label[2]").get_attribute("innerText")
    assert namefiled == "This field is required."
    driver.quit()


#7
def test_when_nameandemail_null():
    driver = init()
    driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[7]/a[1]").click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_5").send_keys(subject)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_2").send_keys(message)
    sleep(2)
    driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()

    namefiled = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/label[2]").get_attribute("innerText")
    assert namefiled == "This field is required."

    emailfiled = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/label[2]").get_attribute("innerText")
    assert emailfiled == "This field is required."
    driver.quit()


8
def test_when_nameandmessage_null():
    driver = init()
    driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[7]/a[1]").click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_5").send_keys(subject)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_4").send_keys(email)
    sleep(2)
    driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()

    namefiled = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/label[2]").get_attribute("innerText")
    assert namefiled == "This field is required."

    messagefiled = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/label[2]").get_attribute("innerText")
    assert messagefiled == "This field is required."

    driver.quit()
#

#9
def test_when_nameemailandmessage_null():
    driver = init()
    driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[7]/a[1]").click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#wpforms-15-field_5").send_keys(subject)
    sleep(2)
    driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()

    namefiled = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/label[2]").get_attribute("innerText")
    assert namefiled == "This field is required."

    emailfiled = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/label[2]").get_attribute("innerText")
    assert emailfiled == "This field is required."

    messagefiled = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/label[2]").get_attribute("innerText")
    assert messagefiled == "This field is required."
    driver.quit()

10
def test_when_allfileds_null():
    driver = init()
    driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[7]/a[1]").click()
    sleep(2)
    driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()

    namefiled = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/label[2]").get_attribute("innerText")
    assert namefiled == "This field is required."

    emailfiled = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/label[2]").get_attribute("innerText")
    assert emailfiled == "This field is required."

    messagefiled = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/label[2]").get_attribute("innerText")
    assert messagefiled == "This field is required."
    driver.quit()

















































