from PIL import Image
from directory_manip import *
def img_compare(image_dict: dict):
    duplicate_count = 0
    image_dict_pixel_data ={}
    for key in image_dict.keys():
        for image in image_dict[key]:

