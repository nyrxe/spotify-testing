
from telnetlib import EC
from Libs import *
    
def LogInOut():
    # create webdriver object
    profile = webdriver.FirefoxProfile('/home/ellenfel/.mozilla/firefox/4bcejejs.4testing')
    driver = webdriver.Firefox(profile)
    # get url
    driver.get("https://open.spotify.com")

    ### logging-in ###
    try:
        driver.implicitly_wait(5)
        login_button = WebDriverWait(driver,10,1).until( EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/header/div[5]/button[2]/div")) )

    except :
        driver.refresh()
        login_button = WebDriverWait(driver,10,1).until( EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/header/div[5]/button[2]")) )

    login_button.click()

    username_field = WebDriverWait(driver,10,1).until( EC.presence_of_element_located((By.ID, "login-username")) )
    username_field.clear()
    username_field.send_keys(username)

    password_field = driver.find_element_by_id("login-password")
    password_field.clear()
    password_field.send_keys(password)

    try:
        driver.find_element_by_id("login-button").send_keys(Keys.ENTER)
    except:
        driver.implicitly_wait(5)
        driver.find_element_by_id("login-button").send_keys(Keys.ENTER)

    #def LogOut():
    ### log-out ###
    pp = WebDriverWait(driver,10,1).until( EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/header/button")) )
   #pp = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[1]/header/button")
    pp.click()

    #/html/body/div[4]/div/div[2]/div[1]/header/div[5]/div/div/ul/li[4]/button
    logout = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[1]/header/div[5]/div/div/ul/li[3]/button")
    logout.click()

    driver.close() #closes the browser
    print("Login & out testing finished successfully")
    driver.quit()