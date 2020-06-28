import io
from tqdm import tqdm
import pyheif
from PIL import Image
import glob

def main():
    files = glob.glob("img/*.HEIC")
    print("\n".join(files))
    for file_name in tqdm(files):
        with open(file_name, "rb") as f:
            convert_heic_to_jpeg(f)

def convert_heic_to_jpeg(f):

    f.seek(0)
    i = pyheif.read_heif(f)

    # Extract metadata etc
    # for metadata in i.metadata or []:
    # if metadata['type']=='Exif':
         # do whatever

    # Convert to other file format like jpeg
    s = io.BytesIO()
    pi = Image.frombytes(mode=i.mode, size=i.size, data=i.data)
    pi.save(s, format="jpeg")

if __name__ == "__main__":
    main()
