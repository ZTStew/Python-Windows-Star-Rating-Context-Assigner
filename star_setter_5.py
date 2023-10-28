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
from mutagen.id3 import POPM, ID3, COMM


parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="*")
args = parser.parse_args()

# Loops through selected files
for file_path in args.files:
  # Rating method for only .mp3 files
  if os.path.splitext(file_path)[1] == ".mp3":
    print(f"Processing: {file_path}")
    audio = ID3(file_path)
    
    try:
      # Changes rating for .mp3 files in POPM format 
      audio['POPM:Windows Media Player 9 Series'].rating = 255
      print(audio)
    except:
      # When a Windows file has metadata, it is wrapped in the POPM object.
      # If there is no metadata, then the POPM object doesn't exist and so the .mp3 file needs to be wrapped in a POPM object

      # Case handles when the non-encapsulated .mp3 file is a TPE2 file
      print("TPE2 File Detected")
      audio.add(POPM(email=audio.get("TPE2").text[0], rating=255))


    print(audio)
    audio.save()

# time.sleep(5)
