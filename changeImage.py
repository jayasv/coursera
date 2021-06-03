import os, sys
from PIL import Image

for root, dirs, files in os.walk("."):
  for file in files:
    f, e = os.path.splitext(file)
    outfile = "supplier-data/images/" + f
    try:
      #print(outfile)
      Image.open(file).resize((128,128)).convert("RGB").save(outfile, "JPEG")

    except IOError:
      print("cannot convert", file)
