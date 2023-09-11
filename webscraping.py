import re
import requests
from bs4 import BeautifulSoup

# Make a GET request to the website to be scraped
url = "https://www.starwars.com"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links in the page and print their href attribute
for link in soup.find_all('a'):
    print(link.get('href'))



#web scraping 



# The URL of the web page you want to extract images from
url = "https://www.starwars.com"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all image tags on the page
img_tags = soup.find_all("img")

# Extract the URLs of the images from the image tags
# img_urls = []
# for img in img_tags:
#     if "src" in img.attrs:
#         img_urls.append(img["src"])




# ...Extract the urls of the image from image tag removing special characters & numbers etc....
img_urls = []
for url in img_urls:
      response = requests.get(url)
      filename = re.sub('[^0-9a-zA-Z]+', '_', url.split("/")[-1])
      with open(filename, "wb") as f:
          f.write(response.content)


# Download each image and save it to a file
for url in img_urls:
    response = requests.get(url)
    with open(url.split("/")[-1], "wb") as f:
        f.write(response.content)


