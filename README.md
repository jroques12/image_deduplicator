# image_deduplicator
Compares all images in a file path to see if they are duplicates.
False positives are a known issue however a secondary filtering method is included to help identify duplicates more definitively.
That being said the program will still move the false positives with the other possible duplicates into a temp folder in the same directory as the image batch.
The primary filtering only compares the first pixel of the image in order to save system memory. This builds a list of images where the first pixel is added
to a dicitonary as the key with the list of images as the value.
This dictionary is then trimmed to only include keys where the list in the value portion is larger than 1 image file.
This short list is then passed to a module to compare image files in each list by collecting the data of 100 pixels every 10th pixel. The likeliness of a 
false positive drastically reduces after this. The first image is used as the base case to compare the rest of the list. If all 100 pixels match, the names
of the image files will be output to the terminal to bring specific attention to those images. All others are likely false positives but are still moved 
to the temp folder for manual comparison.
