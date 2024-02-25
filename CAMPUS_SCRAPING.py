#!/usr/bin/env python
# coding: utf-8

# # CAMPUS CONTACT SCRAPER

# A Python script using requests and BeautifulSoup to scrape and parse HTML content from web pages.

# In[29]:


import requests
from bs4 import BeautifulSoup
import re


# The function fetch_campus_contacts retrieves campus contact information from a given URL. It sends a GET request to the URL, parses the HTML content using BeautifulSoup, and extracts details such as campus names, locations, and contact numbers. It iterates through elements on the page to find campus details, handling cases where certain information might be missing. It uses regular expressions to refine the extraction of contact numbers. The function returns a list of dictionaries containing the extracted information for each campus. If the request fails, it prints a failure message and returns None.
# 

# # To construct the regular expression for Pakistani phone numbers:
# 
# 1. Begin with a non-capturing group (?:...) to encompass variations of the country code.
# 2. Include (?:\+|0{2})92 to match either the country code prefixed with a plus sign or '00' followed by '92'.
# 3. Add an optional group for parentheses around the area code with \(?\d{3}\)?.
# 4. Include [\s.-]? to match optional spaces, dots, or hyphens between number segments.
# 5. Specify \d{3} to match three digits for the area code.
# 6. Add another optional separator with [\s.-]?.
# 7. Include \d{4} to match four digits for the main phone number.
# 8. Use re.findall() to search for all matching instances of this pattern in the text.
# 
# 
# 
# 

# In[30]:


def fetch_campus_contacts(url):
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all campus details
        campus_contacts = []
        
        # Find all elements with campus details
        campus_elements = soup.find_all('div', class_='col-md-4')
            
        # Extract campus names, locations, and contact numbers
        for campus_element in campus_elements:
            campus_name_element = campus_element.find('h4')
            if campus_name_element:
                campus_name = campus_name_element.text.strip()
                
                # Check if address element exists
                address_element = campus_element.find('p')
                campus_location = address_element.text.strip() if address_element else 'Location not available'
                
                # Find the detail div containing contact information
                detail_div = campus_element.find('div', class_='detail')
                if detail_div:
                    # Extract text from detail div
                    detail_text = detail_div.get_text(strip=True)
                    
                    # Extract phone numbers using refined regex
                    contact_numbers = re.findall(r'(?:(?:\+|0{2})92|\(?\d{3}\)?)[\s.-]?\d{3}[\s.-]?\d{4}', detail_text)
                    contact_numbers = ', '.join(contact_numbers)
                else:
                    contact_numbers = 'Contact number not available'
                
                campus_contacts.append({
                    'name': campus_name,
                    'location': campus_location,
                    'contact': contact_numbers
                })
            else:
                print("No campus name found for an element.")
        
        return campus_contacts
    else:
        print("Failed to fetch the webpage.")
        return None


# 
# The provided code retrieves contact information for campuses from the National University (NU) website's "Contact Us" page. It utilizes the fetch_campus_contacts function to scrape the webpage, extracting campus names, locations, and contact numbers. Upon a successful extraction, it prints the details for each campus, including the name, location, and contact information. This code facilitates easy access to campus contacts for individuals interested in reaching out to different NU campuses, providing a convenient and organized display of the relevant information extracted from the website.

# In[31]:


url = 'https://www.nu.edu.pk/home/ContactUs'  # NU website contact us page URL
campus_contacts = fetch_campus_contacts(url)
if campus_contacts:
    print("Campus Contacts:")
    for campus in campus_contacts:
        print(f"Name: {campus['name']}")
        print(f"Location: {campus['location']}")
        print(f"Contact: {campus['contact']}")
        print()


# # NOTE

# This Python script, named "CampusContactScraper.py," is like a digital detective tasked with gathering contact details from the National University (NU) website's "Contact Us" page. It uses special tools called libraries to talk to the website and understand its language. Once it receives permission to access the website (status code 200), it starts examining the website's structure to find the information it needs.
# 
# Imagine the webpage as a complex puzzle, with each piece containing details about different campuses. The script carefully searches through these pieces, known as HTML elements, to find the ones that hold the names, locations, and contact numbers of the campuses. It's like sifting through a stack of papers to find specific bits of information.
# 
# For each campus it discovers, the script grabs the name and location, much like jotting down notes from a bulletin board. It then delves deeper to find the contact details. This part involves looking for a specific section on the webpage where the phone numbers are kept, a bit like finding a phonebook within a library. Once it locates this section, it uses a special technique called regular expressions to identify and extract the phone numbers, making sure to account for different formats they might appear in.
# 
# As the script works its way through the webpage, it keeps track of all the campus details it finds, storing them neatly in a list. If it encounters any issues, like not being able to find a campus name, it lets us know so we can double-check.
# 
# Once it's finished its investigation, the script checks to see if it managed to gather any contact information. If it did, it presents the findings in an easy-to-read format, almost like laying out a map with clear directions. For each campus it discovered, it lists out the name, location, and contact numbers so that anyone looking for this information can easily find it.
# 
# In essence, this script acts as a helpful assistant, taking on the tedious task of collecting campus contact details from the NU website and presenting them in a user-friendly way. It's like having a reliable friend who knows just where to look for the information you need, saving you time and effort.
