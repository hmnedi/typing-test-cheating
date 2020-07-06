# 2020 - 7th - june | After installing selenium and...
from selenium.webdriver import Chrome
import time

# running selenium?
# make sure of your chromdriver path
driver = Chrome(executable_path='chromedriver')
driver.get('http://typesara.com/test')

# instead of using find_elements I used element and a for loop
for i in range(1, 500):
    #   selecting the i-th word
    wordss = driver.find_element_by_xpath(
        "/html/body/section/div/div/div[1]/div/div[3]/div/div/div/div/d"
        "iv[3]/div[1]/div/span[{0}]".format(i))

    #   selecting the textbox
    txtbotx = driver.find_element_by_xpath('//*[@id="inputfield"]')
    #   pasting and pressing the space button
    #   we can press the space button by importing KEYS in selenium too!
    txtbotx.send_keys(wordss.text)
    txtbotx.send_keys(u'\ue00d')
