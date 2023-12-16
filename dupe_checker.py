from PIL import Image
import os


def print_list(list_obj: list, seperator: str):
    for item in list_obj:
        print(item, sep=seperator)


dl = open("dump_log.txt", 'a')
path = r"F:\Jorge's Iphone Photos\iCloud Photos\iCloud Photos\Test Folder"
# creating a list of files from the given path
image_list = os.listdir(path)
# a dict of all the jpeg files as keys with the first pixel's info (cast as tuple) as the value
item_data = {}
# creating a set to add all the first pixel info to check for doubles.
dup_set_identifier = set()
# a dictionary to store the list of possible duplicate file names as keys with the pixel tuple info as the value
duplicate_dict_list = {}

for count, image in enumerate(image_list):

    if image.endswith(".JPEG"):

        # getting the length of the set before trying to add for comparison after
        len_before_add = len(dup_set_identifier)
        # grabbing the image filepath
        next_item = Image.open(path + "\\" + image)
        # creating key value pair using image name and the tuple of the very first pixel of data.
        item_data[image] = tuple(next_item.getdata()[0])
        # attempt to add the tuple to the set.
        dup_set_identifier.add(item_data[image])
        # checking the length of the set after add attempt.
        len_after_add = len(dup_set_identifier)

        # doing the actual comparison of set length before and after add
        # attempt to determine if the current item is a duplicate

        if len_after_add == len_after_add:
            # add the key value pair to a dictionary
            duplicate_dict_list[image] = item_data[image]

        print(f"Loaded {count+1} of {len(image_list)} items")


print(item_data, file=dl)
print("-" * 30 + 'Possible duplicates found: \n', file=dl)
print(duplicate_dict_list, file=dl)

dl.close()
