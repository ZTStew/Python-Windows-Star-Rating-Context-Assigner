"""
Description:
  Program is intended to be run in the Windows Right-Click Context Menu.
  Program will alter the Star Rating of selected files
  Key name: StarSetter
"""

import os, argparse, win32com.client, mutagen
from mutagen.id3 import POPM, ID3

file_path = "C:\\Users\\ZT\\Documents\\_) Programs\\Batch-Programs\\Python-Windows-Star-Rating-Context-Assigner\\Examples\\Soldier.mp3"

# meta = open(f'{file_path}').read()
# print(meta)

# def get_file_description(file_path):
#     description = os.getxattr(file_path, "System.FileDescription")
#     return description

# description = get_file_description(file_path)
# print(f"Description: {description}")

# time.sleep(5)
# print("hi")
# time.sleep(5)

# parser = argparse.ArgumentParser()
# parser.add_argument("files", nargs="*")
# args = parser.parse_args()

# def set_file_rating(file_path, rating):
#     shell = win32com.client.Dispatch("Shell.Application")
#     folder = shell.NameSpace(os.path.dirname(file_path))
#     file = folder.ParseName(os.path.basename(file_path))
#     print("folder: " + str(folder))
#     print("file: " + str(file))
#     folder.SetDetailsOf(file, 266, str(rating))  # Property index for 'System.File.Rating'


# for file_path in args.files:
#   # Your Python script logic here
#   print(f"Processing: {file_path}")

# file_path = "C:\\Users\\ZT\\Documents\\_) Programs\\Batch-Programs\\Python-Windows-Star-Rating-Context-Assigner\\Examples\\aeon 1.jpg"
# new_rating = 5
# set_file_rating(file_path, new_rating)

# time.sleep(5)


# def inspect_file_properties(file_path):
#     shell = win32com.client.Dispatch("Shell.Application")
#     folder = shell.NameSpace(os.path.dirname(file_path))
#     file = folder.ParseName(os.path.basename(file_path))

#     # folder.setDetailsOf(file, 19, 3)
#     property_name = folder.GetDetailsOf(file, 19)
#     # value = folder.GetDetailsOf(file, 19)

#     print(f"Property 19: {property_name} = {value}")

#     # for i in range(266):
#     #   if i != 28 and i != 254:
#     #     property_name = folder.GetDetailsOf(file, i)
#     #     value = folder.GetDetailsOf(file, i)
#     #     print(f"Property {i}: {property_name} = {value}")

# inspect_file_properties(file_path)

"""
Rating Values:
  0 : None
  1 : 1
  2 : 64
  3 : 128
  4 : 196
  5 : 255
"""

audio = ID3(file_path)

print(audio)
print(audio['POPM:Windows Media Player 9 Series'].rating)
audio['POPM:Windows Media Player 9 Series'].rating = 64
print(audio)
audio.save()
print(type(audio))

# for frame in mutagen.File(file_path).tags.getall("POPM:Windows Media Player 9 Series"):
#   print(type(frame))
#   print(frame)
#   print(frame.rating)
#   frame.rating = 64
#   print(frame.rating)
#   # frame.setRating(frame.rating)
#   print(frame)
#   frame.save()

"""
{
  'TSSE': TSSE(encoding=<Encoding.LATIN1: 0>, text=['Lavf58.45.100']),
  'TPE2': TPE2(encoding=<Encoding.LATIN1: 0>, text=['Fleurie']),
  'POPM:Windows Media Player 9 Series': POPM(email='Windows Media Player 9 Series', rating=255)
}
"""