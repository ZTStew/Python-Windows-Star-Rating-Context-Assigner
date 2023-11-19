"""
Description:
  Program is intended to be run in the Windows Right-Click Context Menu.
  Program will alter the Star Rating of selected files
  Key name: StarSetter
"""

import win32com.client
from mutagen.id3 import POPM, ID3, COMM
from mutagen.mp4 import MP4
import os
import ctypes
from datetime import datetime

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

  # Define constants for file properties
  FILE_ATTRIBUTE_DIRECTORY = 0x10
  FILE_ATTRIBUTE_NORMAL = 0x80

  # Define structure for file information
  class FILE_INFO(ctypes.Structure):
    _fields_ = [
      ("dwFileAttributes", ctypes.wintypes.DWORD),
      ("ftCreationTime", ctypes.wintypes.FILETIME),
      ("ftLastAccessTime", ctypes.wintypes.FILETIME),
      ("ftLastWriteTime", ctypes.wintypes.FILETIME),
      ("nFileSizeHigh", ctypes.wintypes.DWORD),
      ("nFileSizeLow", ctypes.wintypes.DWORD),
      ("dwReserved0", ctypes.wintypes.DWORD),
      ("dwReserved1", ctypes.wintypes.DWORD),
      ("cFileName", ctypes.wintypes.LPWSTR),
      ("cAlternateFileName", ctypes.wintypes.LPWSTR),
    ]

  def get_file_properties(file_path):
    # Get file information
    file_info = FILE_INFO()
    result = ctypes.windll.kernel32.GetFileAttributesExW(file_path, 0, ctypes.byref(file_info))
    
    if result == 0:
      print(f"Error {ctypes.windll.kernel32.GetLastError()}: Unable to get file attributes.")
      return

    # Convert file times to a readable format
    creation_time = datetime.utcfromtimestamp((file_info.ftCreationTime.dwHighDateTime << 32) + file_info.ftCreationTime.dwLowDateTime * 1e-7)
    last_access_time = datetime.utcfromtimestamp((file_info.ftLastAccessTime.dwHighDateTime << 32) + file_info.ftLastAccessTime.dwLowDateTime * 1e-7)
    last_write_time = datetime.utcfromtimestamp((file_info.ftLastWriteTime.dwHighDateTime << 32) + file_info.ftLastWriteTime.dwLowDateTime * 1e-7)

    # Print file properties
    print(f"File path: {file_path}")
    print(f"Attributes: {'Directory' if file_info.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY else 'File'}")
    print(f"Creation time: {creation_time}")
    print(f"Last access time: {last_access_time}")
    print(f"Last write time: {last_write_time}")
    print(f"File size: {file_info.nFileSizeLow} bytes")

  # Example usage
  get_file_properties(file_path)



  # try:
  #   with Image.open(file_path) as img:
  #     # Get basic information
  #     format_type = img.format
  #     mode = img.mode
  #     size = img.size
  #     info = img.info
      
  #     # Display information
  #     print(f"Format: {format_type}")
  #     print(f"Mode: {mode}")
  #     print(f"Size: {size}")
  #     print(f"Info: {info}")

  #     # Additional properties specific to JPEG
  #     if format_type == "JPEG":
  #       exif_data = img._getexif()
  #       if exif_data:
  #         for tag, value in exif_data.items():
  #           print(f"EXIF tag {tag}: {value}")
  # except Exception as e:
  #   print(f"Error: {e}")

  # Base registry folder being searched
  # location = winreg.HKEY_LOCAL_MACHINE
  # # Path from location to desired file type
  # # fr'SOFTWARE\Classes\
  # registry_path = "SOFTWARE\\Classes\\.jpg"

  # log += "Location: " + str(location) + "\n"
  # log += "Registry Path: " + registry_path + "\n"
  # print(log)

  # # key_path = r'SOFTWARE\Classes\.txt'
  # # try:
  # #   print(winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, key_path))
  #   # with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, key_path) as key:
  #   #   index = 0
  #   #   while True:
  #   #     try:
  #   #       # Enumerate values in the registry key
  #   #       value_name, value_data, value_type = winreg.EnumValue(key, index)
  #   #       print(f'{value_name}: {value_data} (Type: {value_type})')
  #   #       index += 1
  #   #     except OSError as e:
  #   #       break  # No more values to enumerate
  # # except Exception as e:
  # #   print('Error: ' + str(e))

  # key_path = r'SOFTWARE\Classes\.jpeg'
  # try:
  #   print(winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, key_path))
  # except Exception as e:
  #   print('Error: ' + str(e))




  # try:
    # key = winreg.OpenKey(location, registry_path)
    # print(winreg.QueryValueEx(key, ''))
    # winreg.SetValueEx(key, value_name, reserved, type, value)
    # key: registry key open, in this case, the .jpg key
    # value_name: 'content type', the name of a subkey that has a value
    # reserved: literally does nothing, can be any number, 0 is always read by windows
    # type: Refers to https://docs.python.org/3/library/winreg.html#value-types
    # value: String that specifies new value
    # perceived_type, _ = winreg.QueryValueEx(key, '')
    # print(f'PerceivedType: {perceived_type}')

  # except Exception as e:
  #     print('Error: ' + str(e))
  #     log += 'Error: ' + str(e)


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
