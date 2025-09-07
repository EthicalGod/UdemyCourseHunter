from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import pandas as pd

#udemy URL
URL = 'https://www.udemy.com/'

driver = webdriver.Chrome()
driver.get(URL)

#Code is paused for the given time so you can manually login to your respective Udemy Account
time.sleep(120)

#traverse excel for keywords and max page
file_name = "data.xlsx"
df = pd.read_excel(file_name)
query = df["keywords"].tolist()
max_page = df["maxpage"].tolist()
baseurl = 'https://www.udemy.com/courses/search/?p={}&price=price-free&q={}&src=ukw'


# class to initialize and build each link for selenium traversal
class Extractor:
    def __init__(self, query, max_page):
        # initialize attributes (variables belonging to the object)
        self.max_page = max_page
        self.query = query

    def getdata(query, max_page):
        for i in query:
            baseurl= 'https://www.udemy.com/courses/search/?p={}&price=price-free&q={i}&src=ukw'
            for j in range(1, max_page):
                baseurl = 'https://www.udemy.com/courses/search/?p={j}&price=price-free&q={i}&src=ukw'
                extractdata(baseurl)


    def extractdata(link):
        driver.get(link)
        time.sleep(10)

        maincontainer = driver.find_element("class name", "ud-container")
        card = maincontainer.find_elements("class name", " vertical-card-module--primary--g68s4")
        for c in card:
            title = c.find_element("class name", "card-title-module--clipped--DPJnT")
            rating = c.find_element("class name", "tag-module--tag--4CWOQ")
            url = c.find_element("class name", "ud-btn ud-btn-xsmall ud-btn-secondary ud-heading-sm")
            Data.append({
            "title": title.text.strip(),
            "rating": rating.text.strip(),
            "href": url.get_attribute("href"),
             })


            
# Course Details
Data =[]
driver.quit()
print(Data)