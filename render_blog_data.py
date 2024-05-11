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
<table>
  <tr>
    <th align="left" colspan="2"><a href="{blog['url']}">{blog['title']}</a></th>
  </tr>
  <tr>
    <td width="20%"><a href="{blog['url']}"><img src="{blog['meta_image']}" alt="{blog['title']}" width="100%"></a></td>
    <td width="80%">{blog['meta_description']}</td>
  </tr>
</table>
\n"""


    # Generate the markdown for all blog cards
    rendered_cards = ''.join([generate_blog_card(blog) for blog in blog_data])


    # Append the rendered cards to the README file
    with open('README.md', 'a') as f:
        f.write('\n\n')
        f.write(rendered_cards)

if __name__ == '__main__':
    render_blog_data()