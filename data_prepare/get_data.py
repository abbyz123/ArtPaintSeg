import pathlib, os, shutil
import requests

# get path to api key
curr_path = pathlib.Path.cwd()
path_to_apikey = os.path.join(curr_path, r'../api_key.txt')

# read api_key.txt and get the api key for pixelbay
with open(path_to_apikey) as f:
    api_key = f.readlines()[0]

# read category.txt and get all the categories
path_to_category = os.path.join(curr_path, r'categories.txt')
with open(path_to_category) as f:
    categories = f.readlines()

# download photo for each category
for item in categories:
    url = 'https://pixabay.com/api/?key=' + api_key + '&category=' + item
    req = requests.get(url, timeout=60)
    print(req.content)
