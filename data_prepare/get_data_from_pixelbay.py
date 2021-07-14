import pathlib, os
import requests

# get path to api key
curr_path = pathlib.Path.cwd()
path_to_apikey = os.path.join(curr_path, r'../api_key.txt')

# read api_key.txt and get the api key for pixelbay
with open(path_to_apikey) as f:
    api_key = f.read().splitlines()[0]

# read category.txt and get all the categories
path_to_category = os.path.join(curr_path, r'categories.txt')
with open(path_to_category) as f:
    categories = f.read().splitlines()

# create download folder
path_to_download = curr_path.joinpath(r'../Download')
path_to_train = path_to_download.joinpath('train')
path_to_test = path_to_download.joinpath('test')
path_to_valid = path_to_download.joinpath('valid')
if not os.path.isdir(path_to_download):
    os.mkdir(path_to_download)
if not os.path.isdir(path_to_train):
    os.mkdir(path_to_train)
if not os.path.isdir(path_to_test):
    os.mkdir(path_to_test)
if not os.path.isdir(path_to_valid):
    os.mkdir(path_to_valid)

# download photo for each category
for item in categories:
    url = 'https://pixabay.com/api/?key=' + api_key + '&q=' + item
    req = requests.get(url, timeout=60)
    hit_obj = req.json()['hits']
    for cnt, obj in enumerate(hit_obj, 1):
        jpg_url = obj['largeImageURL']
        jpg_req = requests.get(jpg_url, timeout=60)
        
        # create folder for catetory
        path_to_category = path_to_train.joinpath(item)
        if not os.path.isdir(path_to_category):
            os.mkdir(path_to_category)

        # download the jpg image
        path_to_downloaded_image = path_to_category.joinpath('{}_{}.jpg'.format(item, str(cnt).zfill(8)))
        with open(path_to_downloaded_image, 'wb') as downloaded_image:
            downloaded_image.write(jpg_req.content)
        print('[INFO] downloaded: {}'.format(path_to_downloaded_image))
