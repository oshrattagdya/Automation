from selenium import webdriver

#chrom
# driver = webdriver.Chrome (executable_path="C:/webdriver/chromedriver.exe")
# driver.get("http://www.youtube.com")


#firefox
# driver = webdriver.Firefox(executable_path=(r'../drivers/geckodriver.exe'))
# driver.get("http://www.youtube.com")


#edge
# from selenium.webdriver.common.by import By

driver = webdriver.Edge (executable_path="../drivers/msedgedriver.exe")
# driver.get("http://www.facebook.com")
# driver.find_element(By.XPATH,'//a[contains(text(),"שכחת את הסיסמה?")]').click()
# driver.find_element(By.XPATH,"//a[@id='u_0_2_gd']").click()


driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]").click()
# driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]").click()
# driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]").click()
# driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]").click()