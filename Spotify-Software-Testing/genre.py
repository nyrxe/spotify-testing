from Libs import *

def testGenre():

    # create webdriver object
    profile = webdriver.FirefoxProfile('/home/ellenfel/.mozilla/firefox/4bcejejs.4testing')
    driver = webdriver.Firefox(profile)
    # get url
    driver.get("https://open.spotify.com")

    ### logging-in ###
    try:
        driver.implicitly_wait(5)
        login_button = WebDriverWait(driver,10,2).until( EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/header/div[5]/button[2]/div")) )

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


    ### searching and playing funtionallityies getting tested ###
    search_button = WebDriverWait(driver,10,1).until( EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/nav/div[1]/ul/li[2]/a")) )   
    search_button.click()

    #click the recommended genre
    first_genre = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/div/div/section/div[2]/div/div/a[1]")
    first_genre.click()

    #hover on recomended playlist
    a = ActionChains(driver)
    ele = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[2]/section[1]/div[2]/div[7]/div/div[3]")
    a.move_to_element(ele).perform()

    play_button = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[2]/section[1]/div[2]/div[7]/div/div[1]/div[2]/div/button/div")
    play_button.click()

    driver.close() #closes the browser
    print("Genre Location testings finished successfully")
    driver.quit()