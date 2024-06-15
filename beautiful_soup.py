#!/usr/bin/env python3

# CODE REVISION: Ejimofor Nwoye @ Campaign Lab, Newspeak House, London, 15/06/2024
# DISCLAIMER: Generated with ChatGPT 3.5 OpenAI public LLM, this Python based Web Scraping and data mining software tool is intended for legitimate experimental use, by authorised parties only. Unauthorised, inappropriate and delegated usage, is hereby not implied.
# Remember to always check the terms of service of the website you're scraping from and ensure you're not violating any laws or regulations.

# Web Scraping Using The 'Beautiful Soup' Library

# if you're interested in web scraping with Python, you can use libraries such as BeautifulSoup and Scrapy. Here's a brief overview:
# To install these libraries, you can use pip:
# pip install beautifulsoup4 scrapy

#  **Beautiful Soup**: This library is great for parsing HTML and XML documents. You can extract data from HTML by traversing the DOM tree

from bs4 import BeautifulSoup
import requests

# Fetch the webpage content

url = 'https://www.example.com'
response = requests.get(url)
html_content = response.content

# Parse the HTML

soup = BeautifulSoup(html_content, 'html.parser')

# Find elements by tags, classes, or IDs

title = soup.find('title').text

print(title)
