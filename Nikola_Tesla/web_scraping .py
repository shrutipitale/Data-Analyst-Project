#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install selenium


# In[ ]:


from selenium import webdriver
import pandas as pd


# In[ ]:


pip install requests beautifulsoup4


# In[ ]:


import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    # Send a GET request to the Wikipedia page
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the main sections' titles
        main_sections = soup.find_all('span', {'class': 'mw-headline'})
        section_titles = [section.text for section in main_sections]

        return section_titles
    else:
        # If the request was not successful, print an error message
        print(f"Error: Unable to fetch the page. Status code: {response.status_code}")
        return None

# Example usage
if __name__ == "__main__":
    wikipedia_url = 'https://en.wikipedia.org/wiki/Nikola_Tesla'

    # Run the scraping function
    sections = scrape_wikipedia(wikipedia_url)

    # Print the extracted section titles
    if sections:
        print("Main Sections:")
        for title in sections:
            print(f"- {title}")
    else:
        print("Scraping failed.")


# In[ ]:


import pandas as pd


# In[ ]:


def create_dataframe(data):
  df = pd.DataFrame(data, columns=['Section Titles'])
  return df


# In[ ]:


if sections:
      # Load the data into a Pandas DataFrame
      df = create_dataframe(sections)


# In[ ]:


print(df)


# In[ ]:


df.head()


# In[ ]:


df.shape


# In[ ]:


df.tail(5)


# In[ ]:


pd.isnull(df)


# In[ ]:


get_ipython().system('pip install boilerpipe3')


# In[ ]:


from boilerpipe.extract import Extractor
URL="https://en.wikipedia.org/wiki/Nikola_Tesla"
extrcator=Extractor(extractor='ArticleExtractor',url=URL)
print(extrcator.getText())


# In[5]:


get_ipython().system('pip install feedparser')


# In[6]:


import feedparser


# In[8]:


FEED_URL="https://en.wikipedia.org/wiki/Nikola_Tesla"


# In[17]:


import feedparser

FEED_URL = "https://en.wikipedia.org/wiki/Nikola_Tesla"
fp = feedparser.parse(FEED_URL)


# In[18]:


fp


# In[12]:


dir(feedparser)

