# import os
# def upload(file,thumbnail,title):
#     category = "Comedy" #23
#     description = "The funniest questions and answers from reddit!"
#     tags = "comedy,reddit"
#     finalcommand = ('youtube-upload --title="'+str(title)+'" --description="'+str(description)+'" --tags="'+str(tags)+'" --category="'+str(category)+'" --thumbnail='+str(thumbnail)+' '+str(file))
#     os.system(finalcommand)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os


user=str(os.environ.get("google_email"))
pwd=str(os.environ.get("google_password"))


def login_to_google(username,password,driver):
    driver.get("https://www.youtube.com/upload") # https://accounts.google.com/signin/v2/identifier?service=accountsettings&hl=en-US&continue=https%3A%2F%2Fwww.youtube.com%2Fupload&csig=AF-SEnZufA2NtvyV6QIb%3A1557682200&flowName=GlifWebSignIn&flowEntry=ServiceLogin
    wait = WebDriverWait(driver, 100)
    #assert "Facebook" in driver.title
    wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
    elem_text = driver.find_element_by_id("identifierId")
    elem_text.send_keys(username)
    elem_text.send_keys(Keys.RETURN)

    wait.until(EC.presence_of_element_located((By.ID, "password")))
    elem = driver.find_element_by_name("password")
    elem.send_keys(password)
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    time.sleep(3)
def upload_video(title, thumbnailpath,videopath):
    driver = webdriver.Firefox()
    while 1:
        login_to_google(user, pwd,driver)
        print(driver.current_url)
        if str(driver.current_url) == "https://www.youtube.com/upload":
            break
    wait = WebDriverWait(driver, 100)
    wait.until(EC.presence_of_element_located((By.ID, "upload-prompt-box")))
    elem_upload = driver.find_element_by_xpath(
        "/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[4]/div[1]/div[1]/input")

    # with open("drag_and_drop_helper.js") as f:
    #     js = f.read()
    # DropFile("/home/tom/PycharmProjects/moviepy/test.mp4",elem_upload)
    elem_upload.send_keys(str(videopath))

    wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[3]/form/div[1]/fieldset[3]/div/span[3]/div[2]/div[1]/div/div/input")))
    elem_thumbnail = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[3]/form/div[1]/fieldset[3]/div/span[3]/div[2]/div[1]/div/div/input")
    elem_thumbnail.send_keys(str(thumbnailpath))
    elem_title = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[3]/form/div[1]/fieldset[1]/div/label[1]/span/input")
    elem_title.clear()
    elem_title.send_keys(str(title))
    elem_description = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[3]/form/div[1]/fieldset[1]/div/label[2]/span/textarea")
    elem_description.send_keys("The funniest questions and answers from reddit!")
    elem_publish = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[1]/div[1]/div/div/button")
    elem_publish.click()
    button_content = driver.find_element_by_xpath(
        "/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[1]/div[1]/div/div/button/span")
    print(button_content.get_attribute("innerHTML"))
    print("done")
    # while button_content.text != "Done":
    #     print(button_content.get_attribute("innerHTML"))

    elem_bar = driver.find_element_by_xpath(
        "/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/span/span")
    elem_text_bar = driver.find_element_by_xpath(
        "/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[2]/span[1]")
    elem_bar_progress = driver.find_element_by_xpath(
        "/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[2]/span[1]/span")
    print("uploading")
    while elem_bar.get_attribute("innerHTML") != "100%":
        time.sleep(0.2)
        print(elem_bar.get_attribute("innerHTML"))
    while not "Processing" in str(elem_text_bar.get_attribute("innerHTML")):
        pass
    print("Processing:")
    while elem_bar_progress.get_attribute("innerHTML") != "100%":
        pass
    button = driver.find_element_by_xpath(
        "/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[1]/div[1]/div/div/button")
    button.click()
    time.sleep(0.1)
    driver.close()







