"""
Description:
  Program is intended to be run in the Windows Right-Click Context Menu.
  Program will alter the Star Rating of selected files
  Key name: StarSetter
"""

import os, argparse
from execute import *

# star rating values are not 1, 2, 3. Instead they are based on a value from 0-255. Dictionary converts it to minimize confusion
ratings = {
  "0" : 0,
  "1" : 1,
  "2" : 64,
  "3" : 128,
  "4" : 196,
  "5" : 255
}

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="*")
args = parser.parse_args()


# Loops through selected files
for file_path in args.files:
  if os.path.splitext(file_path)[1] == ".mp3":
    set_stars_mp3(file_path, ratings["1"])