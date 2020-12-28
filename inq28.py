import requests
import time
from pprint import pprint

def print_response_page(response):
    for children in response.get("children"):
        print_reddit_post(children.get("data"))

def print_reddit_post(post):    
    title = post.get("title")
    media = post.get("media")
    if media is not None and media.get("type") is not None and media.get("type") == "imgur.com":
        imgur_url = media.get("oembed").get("url")
        pprint(imgur_url)
        r = requests.get(imgur_url)
        print(r.text)

print("reddit inq28 crawling...")
baseurl = 'https://reddit.com/r/inq28.json?limit=100'
headers = { 'User-Agent': 'inq28 subreddit crawler' }

after = None
while True:
    url = baseurl 
    if after is not None:
        url += "&after=" + after
    r = requests.get(url, headers=headers)
    print("GET " + url)
    response = r.json().get("data")
    print_response_page(response)
    after = response.get("after")
    if after is None:
        break
    time.sleep(2)
