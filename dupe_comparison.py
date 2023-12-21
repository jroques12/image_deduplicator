from PIL import Image
from directory_manip import *


def img_compare(image_dict: dict):
    # opening dumplog txt file
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
        # Closes the dump log
        image_list_pixel_data.clear()


    dl.close()


temp_dict = {(27, 26, 32): ['Scarlet.jpeg', 'Scarlet (2).jpeg', 'Scarlet (1).jpeg'], (33, 32, 28): ['DLAshley.jpg', 'DLAshley (2).jpg', 'DLAshley (1).jpg']}

img_compare(temp_dict)


"""
This 
"""