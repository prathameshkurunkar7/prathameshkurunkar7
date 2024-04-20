import requests
from bs4 import BeautifulSoup
import json
import os

def fetch_blog_data(blog_url):
    response = requests.get(blog_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    meta_description = soup.find('meta', attrs={'name': 'description'})
    meta_description = meta_description.get('content') if meta_description else 'No meta description found'

    meta_image = soup.find('meta', attrs={'property': 'og:image'})
    meta_image = meta_image.get('content') if meta_image else 'No meta image found'

    title = soup.find('title')
    title = title.text.strip() if title else 'No title found'

    blog_data = {
        'meta_description': meta_description,
        'meta_image': meta_image,
        'title': title
    }

    return blog_data

if __name__ == '__main__':
    blog_url = f"{os.environ['BLOG_URL']}?blogger=Prathamesh"
    blog_data = fetch_blog_data(blog_url)

    with open('blog_data.json', 'w') as f:
        json.dump(blog_data, f)