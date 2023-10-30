"""
Description:
  Program is intended to be run in the Windows Right-Click Context Menu.
  Program will alter the Star Rating of selected files
  Key name: StarSetter
"""

from mutagen.id3 import POPM, ID3, COMM
from mutagen.mp4 import MP4


"""
Function: set_stars_mp3
Arugments:
  file_path -> path to file being used
  rating -> new rating of file 
"""
def set_stars_mp3(file_path, rating):
  # Rating method for only .mp3 files
  print(f"Processing: {file_path}")
  audio = ID3(file_path)
  
  try:
    # Changes rating for .mp3 files in POPM format 
    audio['POPM:Windows Media Player 9 Series'].rating = rating
    print(audio)
  except:
    # When a Windows file has metadata, it is wrapped in the POPM object.
    # If there is no metadata, then the POPM object doesn't exist and so the .mp3 file needs to be wrapped in a POPM object

    # Case handles when the non-encapsulated .mp3 file is a TPE2 file
    print("TPE2 File Detected")
    audio.add(POPM(email=audio.get("TPE2").text[0], rating=rating))


  print(audio)
  audio.save()

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
