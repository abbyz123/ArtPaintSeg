import pathlib, os
from zipfile import ZipFile

path_to_dataset = pathlib.Path.cwd().joinpath('..', 'Dataset')
os.chdir(path_to_dataset)

# zipped image file
path_zipped_image_file = path_to_dataset.joinpath('downloads.zip')

# create train, test and valid folders in the dataset
path_train, path_test, path_valid = path_to_dataset.joinpath('train'), path_to_dataset.joinpath('test'), path_to_dataset.joinpath('valid')

# crate train, test, valid folders
if not os.path.isdir(path_train):
    os.mkdir(path_train)
if not os.path.isdir(path_test):
    os.mkdir(path_test)
if not os.path.isdir(path_valid):
    os.mkdir(path_valid)

with ZipFile(path_zipped_image_file, 'r') as zipObj:
    zipObj.extractall(path_train)
