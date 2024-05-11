#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json
import os

def check_if_existing(url):
    # Load existing blog data from JSON file
    try:
        with open("blog_data.json", "r") as f:
            existing_blog_data = json.load(f)
    except FileNotFoundError:
        existing_blog_data = []

    if len(existing_blog_data)==0:
        return

    for blog in existing_blog_data:
        if blog["url"] == url:
            return True
        
    return False
        

def fetch_blog_data(blogs_url):
    response = requests.get(blogs_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    blog_cards = soup.find_all("div", class_="blog-card")

    blogs = []
    for card in blog_cards:
        # Find the link within the card
        link = card.find("a",class_="stretched-link")
        if link:
            # Fetch the linked page
            link_url = link.get("href")
            blog_url = "https://thecommit.company/" + link_url

            # if blog already exists and published then break
            if check_if_existing(blog_url):
                break
            
            link_response = requests.get(blog_url)
            link_soup = BeautifulSoup(link_response.content, "html.parser")

            # Find the meta tags on the linked page
            meta_description = link_soup.find('meta', attrs={'name': 'description'})
            meta_description = meta_description.get('content') if meta_description else 'No meta description found'

            meta_image = link_soup.find('meta', attrs={'property': 'og:image'})
            meta_image = meta_image.get('content') if meta_image else 'No meta image found'

            title = link_soup.find('title')
            title = title.text.strip() if title else 'No title found'

            blog_data = {
                'meta_description': meta_description,
                'meta_image': meta_image,
                'title': title,
                'url': blog_url,
            }

            blogs.append(blog_data)

    return blogs

if __name__ == '__main__':
    blogs_url= os.environ['BLOG_URL']
    blogs = fetch_blog_data(blogs_url)

    if len(blogs) > 0:
        with open('blog_data.json', 'w') as f:
            json.dump(blogs, f)