# pip: Python package installer for Python. We use pip to install and manage software packages written in Python. It connects to the Python Package Index (PyPI) to find and install packages.

# Installing packages with pip

# Numpy: A library for numerical computing in Python
import numpy as np
lst = [1, 2, 3, 4, 5]
np_array = np.array(lst)
print("Numpy Array:", np_array)
print(len(np_array))

# Pandas: A library for data manipulation and analysis
import pandas as pd

# Webbrowser: A library to open web pages in the default browser
import webbrowser
url = "https://www.pokemon.com/us/pokedex/bulbasaur"
webbrowser.open(url)

# To uninstall a package, you can use the following command in the terminal:
# pip uninstall package_name

# To see the list of installed packages, you can use:
# pip list

# To show information about a specific package, you can use:
# pip show package_name

# Pip freeze: Generate installed Python packages with their version and the output is suitable to use it in a requirements file. A requirements.txt file is a file that should contain all the installed Python packages in a Python project.

# Reading from a URL
# To read data from a URL, you can use the `requests` library. First, you need to install it using pip if you haven't already:
# pip install requests
import requests # importing the request module

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page

# Reading from an API
import requests
url = 'https://restcountries.eu/rest/v2/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200 
countries = response.json()
print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries

# Creating a Package
# mypackage

