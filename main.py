import requests
from bs4 import BeautifulSoup
import re
from collections import Counter


def replace_special_characters(input_string):
  # Define a regular expression pattern to match special characters
  pattern = re.compile('[^A-Za-z0-9. ]')

  # Replace special characters with an empty string
  result_string = re.sub(pattern, '', input_string)

  return result_string


# Function to scrape a website
def scrape_website(search,n):
  search = search.replace(' ', '_')

  url = f'https://en.wikipedia.org/wiki/{search}'

  words = ""
  # Send a GET request to the URL
  requests.get(url)
  response = requests.get(url)
  print(response)
  # Check if the request was successful (status code 200)
  if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    # Extract information by navigating the HTML structure
    paragraph = soup.find_all("p")
    for p in paragraph:
      para = replace_special_characters(p.text.strip())
      words = words + para + " "
      # words.join(p.text)

      # text = anchor_tag.text.strip()  # Get the text inside the anchor tag
    # print(words)
    wordArray = words.lower().split()
    word_counts = Counter(wordArray)

    # Get the most common words
    most_common_words = word_counts.most_common(n)

     
    print(most_common_words)
  else:

    print(f"Failed to retrieve the page. Status code: {response.status_code}")


scrape_website("india",100)
