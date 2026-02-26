import json
import os

# Load the links
with open('links.json', 'r') as f:
    links = json.load(f)

# Ensure a directory for redirects exists (optional, or just put in root)
# For this example, we'll put them in the root as 'slug.md'
for slug, destination in links.items():
    content = f"""---
layout: nil
permalink: /{slug}/
redirect_to: "{destination}"
---
"""
    filename = f"{slug}.md"
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created redirect for {slug} -> {destination}")
