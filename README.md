# Background_Changer

This python script gets a random landscape photo by search term and sets it to the desktop background.

# Dependancies 
linux distributions that uses GNOME v3+  
Unsplash API access  
Python3

# Usage
- Set ACCESS_KEY in BackgroundChanger.py to your unsplash api access key
- Set searchTerm in BackgroundChanger.py to your chosen searchTerm 
  - Empty string for a truely random photo
  - For multiple search terms separate by (,) e.g. 'cats,dogs'
  - Use (-) instead of spaces e.g. 'snowy-mountain'
- Set Path in BackgroundChanger.py to choose the path where the photo will be saved
  - Do not add a trailing slash e.g. '/home/matt/BackgroundPhoto'
- run with command python3 BackgroundChanger.py
