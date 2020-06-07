# 2020 - 7th - june | After installing selenium and...
from selenium.webdriver import Chrome
import time
import random

# running selenium?
# make sure of your chromdriver path
driver = Chrome(executable_path='chromedriver')
driver.get('http://typesara.com/test')

# making a list of delay time for not being recognised as a spam Bot????
# You can make an algorithm for a better delay:
# there are 157 words and 60 seconds 60/157=0.38,
#  So the sum of your list shouldn't exceed 0.38
nums = [0.02, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.15, 0.10001, 0.0225]

# instead of using find_elements I used element and a for loop
for i in range(1, 500):
    #   delay
    time.sleep(float(random.choice(nums)))

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
