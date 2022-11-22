import os
import requests
import shutil

def download_file(url, directory,fname=None):
    if fname == None:
        fname = os.path.basename(url)  
    # directory where we store downloaded files 
    new_dl_path = os.path.join(directory, fname) 

    # shutil is efficent for downloading large files
    with requests.get(url, stream=True) as r:
        with open(new_dl_path, 'wb') as f:
            # r.raw because the requests hasnot been closed
            shutil.copyfileobj(r.raw,f)
    return new_dl_path

