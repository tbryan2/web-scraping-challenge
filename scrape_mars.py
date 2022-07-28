# Dependencies
import pandas as pd
import os
import requests
import pymongo
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def scrape():
    # Initialize the Chrome browser session
    driver = webdriver.Chrome()

    # Define URL, navigate to the url
    url = 'https://redplanetscience.com/'
    driver.get(url)

    # Get the html page source and pass it into Beautiful Soup object
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Grab the first article title and teaser, assign them to variables
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    # Define URL, navigate to the url
    url = 'https://spaceimages-mars.com'
    driver.get(url)

    # Get the html page source and pass it into Beautiful Soup object
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Grab the HREF element from the main page image
    featured_image_url = soup.find('a', class_='showimg fancybox-thumbs')['href']

    # Define URL, use pandas to read any table elements on the page
    url = 'https://galaxyfacts-mars.com'
    tables = pd.read_html(url)

    # Define the DataFrame as the first tables element
    df = tables[0]

    # Output the table to html
    html_table = df.to_html()

    # Define URL, navigate to the url
    url = 'https://marshemispheres.com'
    driver.get(url)

    # Get the html page source and pass it into Beautiful Soup object
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Grab the image elements from the page
    hemi_images = soup.find_all('img', class_='thumb')

    # Create an empty dictionary
    hemisphere_image_urls = {}

    # Define a function to add dictionary keys and values
    def add_element(dict, key, value):
        if key not in dict:
            dict[key] = []
        dict[key].append(value)


    # Populate empty dictionary with image alt text and srcs
    for image in hemi_images:
        alt = image.get('alt')
        add_element(hemisphere_image_urls, 'title', alt)
        src = image.get('src')
        add_element(hemisphere_image_urls, 'img_url', src)

    scrape_dict ={
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "html_table": html_table,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    driver.quit()
    return scrape_dict