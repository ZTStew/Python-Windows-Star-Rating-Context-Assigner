"""
Description:
  Program is intended to be run in the Windows Right-Click Context Menu.
  Program will alter the Star Rating of selected files
  Key name: StarSetter
"""

import win32com.client
from mutagen.id3 import POPM, ID3, COMM
from mutagen.mp4 import MP4
import winreg


"""
Function: set_stars_mp3
Arugments:
  file_path -> path to file being used
  rating -> new rating of file 
"""
def set_stars_mp3(file_path, rating):
  return_log = "\n"
  # Rating method for only .mp3 files
  audio = ID3(file_path)
  return_log += "Audio: " + str(audio) + "\n"

  try:
    # Changes rating for .mp3 files in POPM format 
    audio['POPM:Windows Media Player 9 Series'].rating = rating
  except:
    # When a Windows file has metadata, it is wrapped in the POPM object.
    # If there is no metadata, then the POPM object doesn't exist and so the .mp3 file needs to be wrapped in a POPM object

    # Case handles when the non-encapsulated .mp3 file is a TPE2 file
    return_log += "!!! TPE2 File Detected !!!\n"
    audio.add(POPM(email=audio.get("TPE2").text[0], rating=rating))


  return_log += "Rated Audio: " + str(audio) + "\n"
  audio.save()
  return return_log

"""
Function: set_stars_mp4
Arugments:
  file_path -> path to file being used
  rating -> new rating of file 
"""

"""
0-19: No stars (or 0 stars)
20-39: 1 star
40-59: 2 stars
60-79: 3 stars
80-99: 4 stars
100: 5 stars
"""
# Problem, the .mp4 metadata responsible for ratings on Windows does not seem to be editable
def set_stars_mp4(file_path, rating):
  print(f"Processing: {file_path}")
  # video = MP4(file_path)
  # print(video)
  # rating = 100

  # video['rati'] = [str(rating)]

  # print(video)
  # video.save()


"""
Function: set_stars_image
Arugments:
  file_path -> path to file being used
  rating -> new rating of file 
"""
# Despite all attempts, I was unable to programatically effect the star rating of image files
def set_stars_image(file_path, rating):
  print(f"Processing: {file_path}")

  log = ""

  # Base registry folder being searched
  location = winreg.HKEY_LOCAL_MACHINE
  # Path from location to desired file type
  registry_path = "SOFTWARE\\Classes\\.jpg"

  log += "Location: " + str(location) + "\n"
  log += "Registry Path: " + registry_path + "\n"
  print(log)

  try:
    key = winreg.OpenKey(location, registry_path)
    print(winreg.QueryValueEx(key, 'Content Type'))
    # key: registry key open, in this case, the .jpg key
    # 'content type': is a value_name, the name of a subkey that has a value
    # Unused arguments: reserved, type, value
    perceived_type, _ = winreg.QueryValueEx(key, 'Content Type')
    print(f'PerceivedType: {perceived_type}')

  except Exception as e:
      print('Error: ' + e)
      log += 'Error: ' + e


  # registry_path = 

  # file = open(file_path, "w")

  # try:
  #   # Write content to the file
  #   file.write(content)
  # finally:
  #     # Close the file
  #     file.close()

  # with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, file_path) as key:
  #   print(key)


  # try:
  #   shell = win32com.client.Dispatch("Shell.Application")
  #   # Use when not testing
  #   # folder = shell.NameSpace(os.path.dirname(file_path))
  #   # Use when testing
  #   folder = shell.NameSpace(os.path.dirname(os.path.abspath(file_path)))
  #   file = os.path.basename(file_path)

  #   for i in range(0, 266):
  #     # log += str(i) + ": " + folder.GetDetailsOf(file, i) + "\n"
  #     if folder.GetDetailsOf(file, i) == "Rating":
  #       # print("found it")
  #       log += "Rating: " + folder.GetDetailsOf(folder.ParseName(file), i)

  #       # print(file)
  #       file = folder.ParseName(file)
  #       print(file)

  #       file.InvokeVerbEx("setprop", i, "4 Stars")

  #       # folder.GetDetailsOf(file, i) = "5"
  #       # print(folder.GetDetailsOf(file, i))

  #       break

  return log

  #   return "Rating not found"

  # except Exception as e:
  #   print(e)
  #   return f"Error: {str(e)}"
