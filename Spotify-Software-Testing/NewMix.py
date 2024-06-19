from Libs import *

def Mix():
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
        
    ### Create a new mix ###
    newMix_button = WebDriverWait(driver,10,1).until( EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/nav/div[1]/div[2]/div/div[1]/button")) )
    newMix_button.click()

    search_field = WebDriverWait(driver,10,1).until( EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/section/div/div/input")) )
    search_field.clear()
    search_field.send_keys("Selenium")

    add_button = WebDriverWait(driver,10,1).until( EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[1]/div/div[3]/button")) )
    add_button.click()

    source = WebDriverWait(driver,10,1).until( EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/nav/div[1]/div[2]/div/div[5]/div[4]/div/div/ul/div/div[2]/div[1]")) )
    #action chain object
    action = ActionChains(driver)
    action.context_click(source).perform()

    del_button = driver.find_element_by_xpath("/html/body/div[15]/div/ul/li[5]/button")
    del_button.click()

    del_conformation = driver.find_element_by_xpath("/html/body/div[18]/div/div/div/div/button[2]")
    del_conformation.click()

    driver.close() #closes the browser
    print("Creating a new Mix, adding a song & deleting it tested successfully")
    driver.quit()