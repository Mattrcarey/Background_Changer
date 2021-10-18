import requests
from PIL import Image
from io import BytesIO
import os


ACCESS_KEY=''
searchTerm = ''

image_endpoint = f"https://api.unsplash.com/photos/random?query={searchTerm}&page=1&per_page=50&orientation=landscape&client_id={ACCESS_KEY}"
response = requests.get(image_endpoint)
photo = response.json()

download_location = photo['links']['download_location']
payload = {'client_id':ACCESS_KEY}
status_code = requests.get(download_location, payload).status_code

if status_code == 200:
    image_id = photo['id']
    download_endpoint = f"https://api.unsplash.com//photos/{image_id}/download?client_id={ACCESS_KEY}"
    image_download_url = requests.get(download_endpoint).json()['url']
    response = requests.get(image_download_url)
    format = Image.open(BytesIO(response.content)).format # Gets the file type of the image
    filename = f"photo.{format}"
    Image.open(BytesIO(response.content)).save(filename)
    cwd = os.getcwd()
    os.system("gsettings set org.gnome.desktop.background picture-uri file://"+cwd+"/photo." + format)
else:
    print('download not allowed', status_code)
