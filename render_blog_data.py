#!/usr/bin/env python3

import json

def render_blog_data():
    # Load the blog data from the JSON file
    with open('blog_data.json', 'r') as f:
        blog_data = json.load(f)

    # Function to generate the markdown for a single blog card
    def generate_blog_card(blog):
        return f'<a href="{blog["url"]}" target="_blank"><img src="{blog["meta_image"]}" alt="{blog["title"]}" width="300"><h3>{blog["title"]}</h3><p>{blog["meta_description"]}</p></a>'


    # Generate the markdown for all blog cards
    rendered_cards = ''.join([generate_blog_card(blog) for blog in [blog_data]])

    # Wrap the rendered cards in a container
    rendered_cards = f'<div align="center">{rendered_cards}</div>'

    # Append the rendered cards to the README file
    with open('README.md', 'a') as f:
        f.write(rendered_cards)

if __name__ == '__main__':
    render_blog_data()