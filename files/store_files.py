import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(BASE_DIR, "images")

# make files_dir if it doesnot exist
os.makedirs(files_dir, exist_ok=True)

my_images = range(0,10)

for i in my_images:
    fname = f"{i}.txt"
    file_path = os.path.join(files_dir,fname)
    if os.path.exists(file_path):
        print(f"skipped {fname}")
        continue
    with open(file_path, 'w') as f:
        f.write(f"Hello world {i}")