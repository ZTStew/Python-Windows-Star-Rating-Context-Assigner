"""
Description:
  
"""

from execute import *

import os, argparse, time, random
import logging as log
from PIL import Image

log.basicConfig(
    filename=os.path.dirname(os.path.abspath(__file__)) + '\\Log\\star_setter.log',
    level=log.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# log.debug("debug message")
# log.info("info message")
# log.warning("warning message")
# log.error("error message")
# log.critical("critical message")


# star rating values are not 1, 2, 3. Instead they are based on a value from 0-255. Dictionary converts it to minimize confusion
ratings = {
  "0" : 0,
  "1" : 1,
  "2" : 64,
  "3" : 128,
  "4" : 196,
  "5" : 255
}

log.critical("### ### ### V Program Starts V ### ### ###")

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
  help="Specify the file rating [0-5]."
)

args.add_argument(
  "-t",
  "--test",
  type=int,
  help="Declair if the application should run in test mode [0 -> production (default) | 1 -> test mode]."
)

args = args.parse_args()
file_path = args.file
rating = args.rating


if args.test:
  log.critical("Test Running")
  # file_path = "./Examples/jpgtest1.jpg"
  # file_path = "./Examples/jpegtest1.jpeg"
  # file_path = "./Examples/pngtest1.PNG"
  # file_path = "./Examples/mp4test1.mp4"
  file_path = "./Examples/mp3test1.mp3"

  rating = random.randint(0, 5)


log.info("Path: " + file_path)
log.info("Rating: " + str(args.rating))

if os.path.splitext(file_path)[1] == ".mp3":
  log.info("MP3 file detected")
  log.info(set_stars_mp3(file_path, ratings[str(rating)]))


# Does not appear to be possible on Windows *to investigate further*
# if os.path.splitext(file_path)[1] == ".mp4":
#   set_stars_mp4(file_path, ratings["5"])

else:
  def is_image(file_path):
    try:
      with Image.open(file_path) as img:
        return True
    except:
      return False

  if is_image(file_path):
    log.info("Image Detected")
    log.info(set_stars_image(file_path, "5"))
