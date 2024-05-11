#!/usr/bin/env python3

import json

# Function to generate the markdown for a single blog card
# Formatting of the function below is avoided to avoid extra spacing being generated in markdown
def generate_blog_card(blog):
    return f"""
<table>
  <tr>
    <th align="left" colspan="2"><a href="{blog['url']}">{blog['title']}</a></th>
  </tr>
  <tr>
    <td width="20%"><a href="{blog['url']}"><img src="{blog['meta_image']}" alt="{blog['title']}" width="100%"></a></td>
    <td width="80%">{blog['meta_description']}</td>
  </tr>
</table>
"""

def render_blog_data():
    # Load the blog data from the JSON file
    with open('blog_data.json', 'r') as f:
        blog_data = json.load(f)

    # Filter out unpublished blogs
    unpublished_blogs = [blog for blog in blog_data if not blog["published"]]

    # Check if there are any unpublished blog cards
    if len(unpublished_blogs)==0:
        return

    # Generate the markdown for unpublished blog cards
    rendered_cards = '\n'.join([generate_blog_card(blog) for blog in unpublished_blogs])

    # Append the rendered cards to the README file
    with open('README.md', 'a') as f:
        f.write(rendered_cards)

    # Update the published key for the newly rendered blog cards
    for blog in blog_data:
        blog["published"] = True

    # Save the updated blog data to the JSON file
    with open('blog_data.json', 'w') as f:
        json.dump(blog_data, f, indent=2)

if __name__ == '__main__':
    render_blog_data()