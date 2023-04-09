import selenium as se
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import argparse
import bs4
import json

url = 'https://en.wikipedia.org/wiki/Alan_Turing'
options = Options()
browser = wd.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.get(url)
browser.maximize_window()
browser.implicitly_wait(2)
print("Page Title:")
print(browser.title)
print()
dataP = browser.find_elements(by=By.TAG_NAME, value='p')
print("First paragraph containing content:")
for p in dataP:
    if(p.text != ''): 
        print(p.text)
        break
print()
dataTOC = browser.find_element(by=By.XPATH, value='/html/body/div[1]/div/nav/div/div')
print("Table of Contents:")
print(dataTOC.text)
print()
TOCDict = {}
for i, li in enumerate(dataTOC.find_elements(by=By.TAG_NAME, value='li')):
    TOCDict[i+1] = '#' + li.find_element(by=By.TAG_NAME, value='a').get_attribute('href').split('#')[1]
print("Table of Contents Dictionary:")
print(TOCDict)
print()

#create a function that takes a word and looks for it in TOCDict and returns the corresponding value
def findTOC(word : str):
    for key, value in TOCDict.items():
        if(word.upper() in value.upper()):
            return value
    return None

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser(description='find a link')
    parser.add_argument('link', type=str, help='the link to find')

    args = parser.parse_args()

    #find the TOC entry for "Early life"
    print("TOC entry for 'Early life':")
    print(findTOC(args.link))
    if(n:=findTOC(args.link)):
        browser.get(url + n)
        browser.implicitly_wait(5)