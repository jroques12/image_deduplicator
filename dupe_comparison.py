from PIL import Image
from directory_manip import *


def img_compare(image_dict: dict) -> None:

    # opening dump log txt file
    dl = open("dump_log.txt", "w")

    # initializing a list to keep track of image filename and image data as a tuple.
    image_list_pixel_data = []

    # stepping through the keys of a dict
    for key in image_dict.keys():

        # iterating over the list of image names in the given key
        for image in image_dict[key]:

            # opening the image
            image_file = Image.open(PATH + image)

            # grabbing every 10th pixel in the first thousand cast as a tuple.
            current_image_data = tuple(image_file.getdata())[0:1000:10]

            # appends the image info as a tuple in (filename, pixel data tuple) format.
            image_list_pixel_data.append((image, current_image_data))

        # iterating over the duplicates in the pixel data for this batch excluding(slicing) the first entry used as a base case.
        for possible_dup in image_list_pixel_data[1:]:

            # pixel data comparison
            if possible_dup[1] == image_list_pixel_data[0][1]:

                # lists likely duplicates. possible_dup[0] grabs the name of the current image file this iteration
                # image_list_pixel_data[0][0] refers to the name of the image file as the base case
                print(f"Duplicates of {image_list_pixel_data[0][0]} are: {possible_dup[0]}")

        # Outputs the current batch of pixel data to the dump log then clears the list to free up RAM
        print(image_list_pixel_data, file=dl)
        image_list_pixel_data.clear()

    # Closing out the dump log
    dl.close()


"""
This module is intended to do a deeper comparison on top of the initial comparison in the dupe_checker.py file.
Initial comparison only checks the first pixel per image file and flags any duplicates of that pixel. The pixel info
casted as a tuple, is used in a dictionary as the key with a list of image files with that first pixel as the value
That dictionary is then passed to this modules img_compare() function for the deeper analysis. To help identify likely 
false positives which will occur in large batches as in a larger batch of images the first pixel will likely match more,
the img_compare() function will list all matches to the base case, in this way, by exclusion, we can identify the false positives
. This module then takes over the initial filtering by doing a deeper comparison by comparing every 10th pixel of the first thousand pixels to the base case (first image
file in the value portion of the dictionary per corresponding key. So as to encourage the end user to do a closer 
manual comparison of the initial filtering (aka "short list") the program does not then go and prevent the false
positives from being added to the temp folder. It will however list all the files that are duplicates of the secondary
filtering when compared to the base case. There is a possibility of a false positive being the base case in which none
of the other possible duplicates will be explicitly flagged in the terminal. This is another reason for including them
in the temp folder move.
"""