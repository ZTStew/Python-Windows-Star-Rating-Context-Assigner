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

file_path = ".\\Examples\\115.mp3"

# parser = argparse.ArgumentParser()
# parser.add_argument("files", nargs="*")
# args = parser.parse_args()

# for file_path in args.files:
  # Your Python script logic here
if os.path.splitext(file_path)[1] == ".mp3":
  print(f"Processing: {file_path}")

  audio = ID3(file_path)
  print(audio)
  
  try:
    audio['POPM:Windows Media Player 9 Series'].rating = 128
    print(audio)
  except:
    print("non-popm file")
    print("###################################################")
    # audio.add(COMM(encoding=3, rating=128))
    # audio['POPM:Windows Media Player 9 Series'].rating = 128

    tpe2_frame = audio.get("TPE2")
    tpe2_value = tpe2_frame.text[0]

    popm_frame = POPM(email=tpe2_value, rating=128)
    audio.add(popm_frame)

    print(audio)
    audio.save()

    print("###################################################")

# time.sleep(5)



# print(audio['POPM:Windows Media Player 9 Series'].rating)
# print(audio)
# print(type(audio))
