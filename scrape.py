# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 21:45:38 2020

@author: stany
"""
import requests # Creating the "get" query
from bs4 import BeautifulSoup # Creates a parsed and navigable HTML document
url = "http://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')   # Using the lxml parser for HTML
quotes = soup.find_all('span', class_='text') # Contains a list of all the elements
                                              # and class 'text' 
                                             
authors = soup.find_all('small', class_='author')                                              # on the HTML website with the tag 'span' 

# Each individual tag for each quote has a tag 'a' and a class 'tag', which 
# would return all tags but make it impossible to match them to a specific quote.  

# Instead, we know that each set of tags for each quote is contained within the 
# section that is defined by the 'div' tag and 'tags' class.  
tags = soup.find_all('div', class_='tags') 
                                             
                                              
''' Prints the entire HTML doc for the quotes web page '''                                    
#print(soup) 

''' Prints all the quotes as a list, ableit with a little HMTL info attached '''
#print(quotes) 

''' Print all the quotes without the HTML info '''
#for quote in quotes:
#    print(quote.text)
    
''' Print all quotes with their author ''' 
for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a', class_='tag') # We isolate each set of tags for each quote here.  
    for quoteTag in quoteTags:
        print(quoteTag.text) # This prints each tag we isolated for the specific quote. 