"""
Description:
  Program is intended to be run in the Windows Right-Click Context Menu.
  Program will alter the Star Rating of selected files
  Key name: StarSetter
"""

"""
Rating Values:
  0 : None
  1 : 1
  2 : 64
  3 : 128
  4 : 196
  5 : 255
"""
import os, argparse, time
from mutagen.id3 import POPM, ID3

file_path = ".\\Examples\\10.mp3"

# parser = argparse.ArgumentParser()
# parser.add_argument("files", nargs="*")
# args = parser.parse_args()

# for file_path in args.files:
  # Your Python script logic here
if os.path.splitext(file_path)[1] == ".mp3":
  print(f"Processing: {file_path}")

  audio = ID3(file_path)
  print(audio)
  
  # audio['POPM:Windows Media Player 9 Series'].rating = 128
  # audio.save()

# time.sleep(5)



# print(audio['POPM:Windows Media Player 9 Series'].rating)
# print(audio)
# print(type(audio))
