"""
Description:
  Attempt to add additional variables to the registry so that a single .exe file would need to be compiled.
  Status: Failed
"""

from execute import *

import os, argparse, time
from PIL import Image

# star rating values are not 1, 2, 3. Instead they are based on a value from 0-255. Dictionary converts it to minimize confusion
ratings = {
  "0" : 0,
  "1" : 1,
  "2" : 64,
  "3" : 128,
  "4" : 196,
  "5" : 255
}

print('here')

args = argparse.ArgumentParser()
args.add_argument("--files")
args.add_argument("--rating")
args = args.parse_args()

print(args)

# file_path = "./Examples/jpgtest1.jpg"
# file_path = "./Examples/jpegtest1.jpeg"
# file_path = "./Examples/pngtest1.PNG"
# file_path = "./Examples/mp3test1.mp3"
# file_path = "./Examples/mp4test1.mp4"

# Loops through selected files
# for file_path in args.files:
if os.path.splitext(args.files)[1] == ".mp3":
  set_stars_mp3(args.files, ratings[str(args.rating)])

time.sleep(10)

# Does not appear to be possible on Windows *to investigate further*
# if os.path.splitext(file_path)[1] == ".mp4":
#   set_stars_mp4(file_path, ratings["5"])

# else:
#   def is_image(file_path):
#     try:
#       with Image.open(file_path) as img:
#         return True
#     except:
#       return False

#   set_stars_image(file_path, "5")
