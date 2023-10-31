"""
Description:
  
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


args = argparse.ArgumentParser()
args.add_argument(
  "-f",
  "--file",
  type=str,
  help="Specify the file name."
)
args.add_argument(
  "-r",
  "--rating",
  type=int,
  help="Specify the file name."
)

args = args.parse_args()

# file_path = "./Examples/jpgtest1.jpg"
# file_path = "./Examples/jpegtest1.jpeg"
# file_path = "./Examples/pngtest1.PNG"
# file_path = "./Examples/mp3test1.mp3"
# file_path = "./Examples/mp4test1.mp4"

if os.path.splitext(args.file)[1] == ".mp3":
  set_stars_mp3(args.file, ratings[str(args.rating)])


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
