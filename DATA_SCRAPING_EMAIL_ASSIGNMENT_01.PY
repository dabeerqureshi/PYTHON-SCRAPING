#!/usr/bin/env python
# coding: utf-8

# # Scraping All Emails of All FAST NUCES CAMPUSES

# This Python script utilizes the requests library to fetch the HTML content of a webpage, then utilizes BeautifulSoup and re to parse and extract data from the HTML.

# In[3]:


import re
import requests
from bs4 import BeautifulSoup


# This variable url contains the web address for the contact page of the National University website.

# In[ ]:


# URL of the NU website
url = 'https://www.nu.edu.pk/home/ContactUs'


# 
# This code sends a GET request to the specified URL, retrieves the HTML content of the webpage, and stores it in the variable html_content.

# In[ ]:


# Fetch the HTML content of the website
response = requests.get(url)
html_content = response.text


# 
# This code utilizes BeautifulSoup library to parse the HTML content retrieved from the website, enabling further extraction and manipulation of its elements.

# In[ ]:


# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')


# 
# This code extracts all the visible text content from the parsed HTML using BeautifulSoup and stores it in the variable text.

# In[ ]:


# Find all text within the HTML content
text = soup.get_text()


# This regular expression pattern (email_pattern) is designed to match email addresses within a text.
# 1. It starts with \b to denote a word boundary.
# 2. [A-Za-z0-9._%+-]+ matches one or more alphanumeric characters, dots, underscores, percentage signs, plus signs, or hyphens, which are common characters in email addresses.
# @ matches the "@" symbol.
# 3. [A-Za-z0-9.-]+ matches one or more alphanumeric characters, dots, or hyphens, which are typically found in the domain part of email addresses.
# 4. \. matches a dot, which separates the domain name from the top-level domain (TLD).
# 5. [A-Z|a-z]{2,} matches the TLD, ensuring it consists of at least two letters, whether uppercase or lowercase.
# 6. \b again denotes a word boundary, ensuring the match ends correctly.

# In[ ]:


# Regular expression pattern to match email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


# 
# This code utilizes the defined regular expression pattern to find all email addresses within the extracted text and stores them in the variable emails.

# In[ ]:


# Find all email addresses in the text using the regular expression
emails = re.findall(email_pattern, text)


# 
# This loop iterates over each email address in the emails list and prints each one individually.
# 
# 
# 
# 
# 

# In[ ]:


# Print the extracted email addresses
for email in emails:
    print(email)


# The Python script provided performs web scraping to extract email addresses from the contact page of the National University (NU) website. Initially, the script employs the requests library to fetch the HTML content of the specified URL, storing it in the variable html_content. Subsequently, utilizing the BeautifulSoup library, the HTML content is parsed into a BeautifulSoup object named soup, facilitating efficient traversal and manipulation of HTML elements. The script then extracts all visible text content from the parsed HTML using the soup.get_text() method, consolidating it into the variable text. To identify email addresses within the extracted text, a regular expression pattern (email_pattern) is defined, ensuring accurate matching based on common email formatting conventions. The re.findall() function is subsequently employed with the defined email_pattern to search for and extract all email addresses present in the text, storing the matches in the emails variable as a list. Finally, a loop iterates over each extracted email address in the emails list, printing them individually. This script exemplifies a basic yet effective approach to web scraping, demonstrating the utilization of Python libraries to programmatically extract desired information from web pages, in this case, email addresses from the NU contact page.
