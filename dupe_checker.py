from PIL import Image
from directory_manip import *


def print_list(list_obj: list, seperator: str):
    for item in list_obj:
        print(item, sep=seperator)


# opening dump log
dl = open("dump_log.txt", 'w')
# designating file path preference for windows and linux. Note: need to change direction of slash in further code
win_path = r"F:\Jorge's Iphone Photos\iCloud Photos\iCloud Photos\Test Folder"
lin_path = r"/home/scrant/"
# creating a list of files from the given path
image_list = os.listdir(PATH)
print(image_list)
# a dict of all the jpeg files as keys with the first pixel's info (cast as tuple) as the value
item_data = {}
# creating a set to add all the first pixel info to check for doubles.
dup_set_identifier = set()
# a dictionary to store the list of possible duplicate file names as keys with the pixel tuple info as the value
duplicate_dict_list = {}
# a set to hold the touples that are duplicates
duplicate_set_list = set()
# the final dictionary of duplicates
final_duplicates_dict = {}

# iterating over the list of image files in the given path.
for count, image in enumerate(image_list):

    if image.endswith(".jpeg") or image.endswith(".jpg"):

        # getting the length of the set before trying to add for comparison after
        len_before_add = len(dup_set_identifier)
        # grabbing the image filepath
        next_item = Image.open(PATH + image)
        print(PATH+image)
        # creating key value pair using image name(values) and the tuple of the very first pixel of data (keys).
        # This will cause
        # certain images to mistakenly be grouped as duplicates due to having the exact same first pixel despite being
        # different images. This was intended as loading even just a handful of images simultaneously will cause a RAM
        # related crash. Once the "short list" is generated, will filter additionally to exclude these edge cases.
        item_data[image] = tuple(next_item.getdata())[0:100]
        # attempt to add the tuple to the set.
        dup_set_identifier.add(item_data[image])
        # checking the length of the set after add attempt.
        len_after_add = len(dup_set_identifier)

        # doing the actual comparison of set length before and after add
        # attempt to determine if the current item is a duplicate

        if len_before_add == len_after_add:
            # add the key value pair to a dictionary
            duplicate_dict_list[image] = item_data[image]
            # add the tuple to a set to account for the pixels with duplicates
            duplicate_set_list.add(item_data[image])

        # iterating over the duplicate set list and building the final duplicate list including the originals
        for set_item in duplicate_set_list:
            final_duplicates_dict[set_item] = []
            for key, value in item_data.items():
                if value == set_item:
                    final_duplicates_dict[set_item].append(key)

        # need to take the values from duplicate_dict_list to get the originals

        print(f"Loaded {count+1} of {len(image_list)} items")

# iterating over the keys which are first pixel info as a tuple to determine if more than 1 image is assocaited with it
# and moving those images to a temporary folder for comparison and further filtering.
for key in final_duplicates_dict.keys():
    if len(final_duplicates_dict[key]) > 1:
        for file in final_duplicates_dict[key]:
            move_to_path(PATH + file, PATH + 'temp')

# outputting all the relevant data to a txt file with some decoration
print("_" * 30 + "All data in filepath: " + "-" * 30, file=dl)
print(item_data, file=dl)
print("-" * 30 + 'Possible duplicates found:' + "-" * 30 + '\n', file=dl)
print(duplicate_dict_list, file=dl)
print("Finale Duplicate Dict", file=dl)
print(final_duplicates_dict, file=dl)

dl.close()

"""
Was able to successfully implement a dynamic path variable in directory_manip to account for OS differences for linux
and windows.
"""