from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def init():
    driver = webdriver.Chrome('..\drivers\chromedriver.exe')
    driver.get("https://atid.store/about/")
    driver.maximize_window()
    return driver

#UI TESTING FOR ABOUT_US PAGE
#1
def test_upper_Menubar_():
    driver = init()
    driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[6]/a[1]").click()

    upperMenubar = driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]").get_attribute("innerText")
    assert upperMenubar == "HOME\nSTORE\nMEN\nWOMEN\nACCESSORIES\nABOUT\nCONTACT US\nSearch\n0.00 ₪ 0"
    driver.quit()

#2
def test_title_aboutus():
    driver = init()
    titleaboutus = driver.find_element(By.XPATH,"//h1[contains(text(),'About Us')]").get_attribute("innerText")
    assert titleaboutus == "About Us"
    driver.quit()

#3
def test_title_whoweare():
    driver = init()
    titlewhoweare = driver.find_element(By.XPATH,"//h2[contains(text(),'Who We Are')]").get_attribute("innerText")
    assert  titlewhoweare == "Who We Are"
    driver.quit()

#4
def test_paragraph():
    driver = init()
    paragraph = driver.find_element(By.XPATH,"//p[contains(text(),'ATID Demo Store was created by ATID College dedica')]").get_attribute("innerText")
    assert paragraph == "ATID Demo Store was created by ATID College dedicated employees. This is a complete demo site for practicing QA & Test Automation methodologies. Don't think for a second you can actually buy here something cause you can't ! This Demo Store contains software bugs which were put intentionally and your job is to locate them Good luck falks, Yoni Flenner - ATID College"
    driver.quit()

#5
def test_title_fewwords():
    driver = init()
    titlefewworeds = driver.find_element(By.XPATH,"//h4[contains(text(),'A Few Words About')]").get_attribute("innerText")
    assert titlefewworeds == "A Few Words About"
    driver.quit()

#6
def test_ourTeam_title():
    driver = init()
    ourteamtitle = driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[3]/div[1]").get_attribute("innerText")
    assert ourteamtitle == "Our Team\n\nWe have the best team ever everybody who is somebody wants to work with us, so we can afford cherry-picking them, one by one..."
    driver.quit()


#7
def test_Teammembers():
    driver = init()
    teammembers = driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[3]").get_attribute("innerText")
    assert teammembers == "Yoni Flenner\n\nFounder - CEO\n\nAlbert Einstein\n\nCOO\n\nSteve Jobs\n\nMarketing Head\n\nBill Gates\n\nLead Developer\n\nKim Kardashian\n\nIntern Designer\n\nMadonna\n\nHead of Fun"
    driver.quit()

#8
def test_followus():
    driver = init()
    followus = driver.find_element(By.XPATH,"//h2[contains(text(),'Follow Us')]").get_attribute("innerText")
    assert followus == "Follow Us"
    driver.quit()


#9
def test_lowerpage():
    driver = init()
    lowerpage = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[5]").get_attribute("innerText")
    assert lowerpage == "Worldwide Shipping\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nBest Quality\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nBest Offers\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nSecure Payments\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo."
    driver.quit()


#links testing for about us page
#10
def test_facebooklink():
    driver = init()
    facebooklink = driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[4]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/span[1]/a[1]").get_attribute("innerText")
    assert facebooklink ==  "Facebook-f"
    driver.quit()


#11
def test_twiterlink():
    driver = init()
    twiterlink = driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[4]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]").get_attribute("innerText")
    assert twiterlink == "Twitter"
    driver.quit()


#12
def test_instagramlink():
    driver = init()
    instagramlink = driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[4]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/span[3]").get_attribute("innerText")
    assert instagramlink == "Instagram"
    driver.quit()


#13
def test_googlelink():
    driver = init()
    googlelink = driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[4]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/span[4]").get_attribute("innerText")
    assert googlelink == "Google-plus-g"
    driver.quit()


#14
def test_quicklinks():
    driver = init()
    quicklinks = driver.find_element(By.XPATH,"//section[@id='nav_menu-1']").get_attribute("innerText")
    assert quicklinks == "Quick Links\nHome\nAbout\nCart\nContact Us"
    driver.quit()


#15
def test_forher():
    driver = init()
    forher = driver.find_element(By.XPATH,"//section[@id='nav_menu-2']").get_attribute("innerText")
    assert forher == "For Her\nWomen Jeans\nTops and Shirts\nWomen Jackets\nHeels and Flats\nWomen Accessories"
    driver.quit()


#16
def test_forhim():
    driver = init()
    forhim = driver.find_element(By.XPATH,"//section[@id='nav_menu-3']").get_attribute("innerText")
    assert forhim == "For Him\nMen Jeans\nMen Shirts\nMen Shoes\nMen Accessories\nMen Jackets"
    driver.quit()

#ikon testing

#17
def test_appstore_ikon():
    driver = init()
    appstoreikon = driver.find_element(By,"//section[@id='media_image-1']").get_attribute("innerHTML")
    assert appstoreikon == "<img width=\"144\" height=\"44\" src=\"https://atid.store/wp-content/uploads/2021/06/appstore-img.png\" class=\"image wp-image-2818  attachment-full size-full\" alt=\"\" loading=\"lazy\" style=\"max-width: 100%; height: auto;\">"
    driver.quit()


#18
def test_googleplay_ikon():
    driver = init()
    googleplayikon = driver.find_element(By.XPATH,"//section[@id='media_image-2']").get_attribute("innerHTML")
    assert googleplayikon == "<img width=\"144\" height=\"44\" src=\"https://atid.store/wp-content/uploads/2021/06/appstore-img.png\" class=\"image wp-image-2818  attachment-full size-full\" alt=\"\" loading=\"lazy\" style=\"max-width: 100%; height: auto;\">"
    driver.quit()


def test_buttomline():
    driver = init()
    buttomline = driver.find_element(By.XPATH,"//body/div[@id='page']/footer[@id='colophon']/div[2]").get_attribute("")