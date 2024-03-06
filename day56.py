# Create a function to extract all URLs from a given text using regular expressions

import re

def extract_urls(text):
    return re.findall(r'(https?://[^\s]+)', text)

text = "URLs to test: http://google.com https://google.com https://www.google.com https://google.com/news"
print(extract_urls(text))