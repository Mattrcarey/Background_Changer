import requests
from PIL import Image
from io import BytesIO
import os


ACCESS_KEY=''
searchTerm = ''
path = ''

image_endpoint = f"https://api.unsplash.com/photos/random?query={searchTerm}&page=1&per_page=10&orientation=landscape&client_id={ACCESS_KEY}"
response = requests.get(image_endpoint)
photo = response.json()

download_location = photo['links']['download_location']
payload = {'client_id':ACCESS_KEY}
response = requests.get(download_location, payload)
status_code = response.status_code

if status_code == 200:
    image_id = photo['id']
    image_download_url = response.json()['url']
    response = requests.get(image_download_url)
    format = Image.open(BytesIO(response.content)).format # Gets the file type of the image
    filename = f"{path}/photo.{format}"
    Image.open(BytesIO(response.content)).save(filename)
    os.system("gsettings set org.gnome.desktop.background picture-uri file://"+filename)
else:
    print('download failed', status_code)
