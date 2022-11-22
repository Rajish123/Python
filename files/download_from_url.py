import requests
import os
import shutil
from download_util import download_file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# for small item
downloaded_img_path = os.path.join(DOWNLOAD_DIR, '1.jpg')
url = "https://i.pinimg.com/236x/71/28/3b/71283bb49db55cfee5bb6acd1389c465--tree-of-life-the-tree.jpg"

# stream=True will keep this url open until we get this data done
r = requests.get(url, stream=True)
# if not 200 status, then will run an error
r.raise_for_status()

with open(downloaded_img_path, 'wb') as f:
    # r.contents will give whatever the above requests sends back
    f.write(r.content)
    

download_file(url, DOWNLOAD_DIR)