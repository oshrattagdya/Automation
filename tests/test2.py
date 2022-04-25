from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#יצרת פונקציית התחברות לדפדפן ופרטי אתר
def init():
    driver = webdriver.Chrome('..\drivers\chromedriver.exe')
    driver.get("https://atid.store/")
    driver.maximize_window()
    return driver

#home
# driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]").click()

#יוצרת משתנה בשם דרייב ומכניסה בו את הערכים של INIT
#ואז נכנסת לאלמנטים שרוצה ומבצעת פעולות

def search_in_store():
    driver = init()
    driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]").click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#wc-block-search__input-1").send_keys("t-shirt")
    sleep(2)
    driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]").click()
    value = driver.find_element(By.XPATH,"//main[1]/div[1]/p[1]").get_attribute("innerText")
    assert value == "No products were found matching your selection."



#קוראת לפונקציה כדי להפעיל אותה
search_in_store()


# #men
# def search_in_men():
#     driver=init()
#     driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]").click()
#     sleep(5)
#     driver.find_element(By.CSS_SELECTOR,"#wc-block-search__input-1").send_keys("t-shirt")
#     sleep(5)
#     driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]").click()
#     driver.quit()
#
# search_in_men()

# #women
# def search_in_womeman():
#     driver = init()
#     driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]").click()
#     sleep(5)
#     driver.find_element(By.CSS_SELECTOR,"#wc-block-search__input-1").send_keys("t-shirt")
#     sleep(5)
#     driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]").click()
#     driver.quit()
#
#
# search_in_womeman()