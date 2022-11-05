"""
STATUS: Working

OVERVIEW: Use [Beautiful Soup] for web scrapping, downloads all the images of a website page

IMPROVEMENTS:

TODO Document

Workings:
    1. Importing
        1. beautiful-soup for accessing web
        2. Request for getting the json and images
        3. os for saving the images in a certain location
    2. ExtractPanels
        ** This function will extract images from the web pages link we have given and then save the images with the index name in specified folder
"""

# @ Imports
from bs4 import *
import requests as request
import os

# * Defining

images_folder_path = 'E:\Coding\Projects\Images Extractor\Database'

def ExtractPanels(url, images_folder_path, index_t=''):
    """
        What is done:
            1. Obtaining webpage data in JSON format using requests module
            2. Making this JSON into a BeautifulSoup object
            3. Making a mock list for storing the links
            4. Using the soup object obtaining the images data with common link format
            5. Using this data adding the links of the images in the images list
            6. Changing the dir for image saving conviniences
            7. Looping through all the links in the images_links list
                1. Opening try & except for error handling
                2. form each link we will be obtaining the content => image
                3. Opening a file with the link index in the list
                4. And saving the image in jpg format
                ** printing success message
    """
    webpage_object = request.get(url)
    soup = BeautifulSoup(webpage_object.text, "html.parser")

    images_links = []

    # images_data = soup.select(f'img[src^={CommonInLink(url)}]' if CommonInLink(url) else 'img[src]')
    images_data = soup.select('img[src]')

    for image in images_data:
        images_links.append(image['src'])

    os.chdir(images_folder_path)

    for index, image_link in enumerate(images_links, 1):
        try:
            image_data = request.get(image_link).content

            with open(f'{index}.jpg', 'wb+') as f:
                print(f'panel_{index if not index_t else index_t}.jpg sucessfully made! > Extractor')
                f.write(image_data)

        except Exception as exception:
            print(exception)
            print(f'{image_link} > Images_Extractor')

def CommonInLink(url):
    """
    """
    pass
    r2 = request.get(url)
    soup2 = BeautifulSoup(r2.text, "html.parser")

    links = []

    x = soup2.select('img[src]')

    for img in x:
        links.append(img['src'])

    return Common_Strings(links)

# ? Implementation
if __name__ == "__main__":
        url = f'https://greekgodsandgoddesses.net/gods/'
        ExtractPanels(url, images_folder_path)
