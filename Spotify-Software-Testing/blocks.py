from Libs import *

def block():
    # create webdriver object
    profile = webdriver.FirefoxProfile('/home/ellenfel/.mozilla/firefox/4bcejejs.4testing')
    driver = webdriver.Firefox(profile)
    # get url
    driver.get("https://open.spotify.com")

    ### searching and playing funtionallityies getting tested ### 
    lib_button = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/nav/div[1]/ul/li[3]/div/a")
    lib_button.click()


    liked_button =driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/nav/div[1]/div[2]/div/div[2]/a")
    liked_button.click()

    logIn_button =driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/nav/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div[2]/button[2]")
    logIn_button.click()

    driver.close() #closes the browser
    print("blocking funcs tested successfully")
    driver.quit()