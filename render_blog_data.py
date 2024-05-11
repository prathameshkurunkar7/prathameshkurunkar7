#!/usr/bin/env python3

import json

def render_blog_data():
    # Load the blog data from the JSON file
    with open('blog_data.json', 'r') as f:
        blog_data = json.load(f)

    # Function to generate the markdown for a single blog card
    # Formatting of the function below is avoided to avoid extra spacing being generated in markdown
    def generate_blog_card(blog):
        return f"""\n
<a href="{blog["url"]}" target="_blank" style="text-decoration: none !important; color: inherit !important;">
<div style="display: flex; align-items: center; border-radius: 4px; border: 1px solid #30363d; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); overflow: hidden; max-height: 200px;">
<div style="max-width: 33.33%;">
<img src="{blog["meta_image"]}" alt="{blog["title"]}" style="width: 100%; border-radius:4px">
</div>
<div style="padding: 16px;">
<h2 style="font-size: 18px; font-weight: bold; margin-bottom: 10px;">{blog["title"]}</h2>
<p style="font-size: 14px; line-height: 1.5; margin-bottom: 14px;">{blog["meta_description"]}</p>
</div>
</div>
</a>\n"""


    # Generate the markdown for all blog cards
    rendered_cards = ''.join([generate_blog_card(blog) for blog in blog_data])

    # Wrap the rendered cards in a container
    rendered_cards = f'<div style="display: flex; flex-direction: column; gap: 8px">{rendered_cards}</div>'

    # Append the rendered cards to the README file
    with open('README.md', 'a') as f:
        f.write('\n\n')
        f.write(rendered_cards)

if __name__ == '__main__':
    render_blog_data()