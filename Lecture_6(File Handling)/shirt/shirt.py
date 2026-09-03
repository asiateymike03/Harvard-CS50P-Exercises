import os
from PIL import Image, ImageOps
import sys

# checking for few cmd-line arguments
if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments.")

# checking for many cmd-line arguments
if len(sys.argv) >= 4:
    sys.exit("Too many command-line arguments.")

extensions = {".jpeg", ".jpg", ".png"}
# checking if input is valid
if os.path.splitext(sys.argv[1])[1].lower() not in extensions:
    sys.exit("Invalid output")

# checking if output is valid
if os.path.splitext(sys.argv[2])[1].lower() not in extensions:
    sys.exit("Invalid output")

# checking file extensions compatibility
if os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
    sys.exit("Input and output have different extensions")

try:
    muppet = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    new_image = ImageOps.fit(muppet, (600, 600), centering=(0, 0.5))
    new_image.paste(shirt, shirt)
    new_image.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")



