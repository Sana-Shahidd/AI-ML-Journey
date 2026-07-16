
# Web Scraping
# we will practically implement MultiThreading in Web scraping
# We will use Libraries like requests for HTTPS responses and Requests & bs4 -->> beautifulSoup for scrapping
import threading
import requests
from bs4 import BeautifulSoup
# Basic scrapper 

urls = [
    "https://www.python.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.wikipedia.org"
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content, "html.parser")
    print(f"Fetched{len(soup.text)} characters from {url}")

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("all webpages data fetched")