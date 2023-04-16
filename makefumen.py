import cv2
from PIL import Image
import os
from natsort import natsorted

video = "bad apple.mp4"
folder = "badframes"
compressed_folder = "badcompressed"
vidcap = cv2.VideoCapture(video)
success,image = vidcap.read()
count = 0

if not os.path.exists(folder):
    os.makedirs(folder)

while success:
  cv2.imwrite(f"{folder}/frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  count += 1

print("video is split")

if not os.path.exists(compressed_folder):
    os.makedirs(compressed_folder)

for filename in os.listdir(folder):
    image_path = os.path.join(folder, filename)
    with Image.open(image_path) as image:
        image = image.resize((10, 10), resample=Image.BICUBIC)

        output_filename = f"compressed_{filename}"
        output_path = os.path.join(compressed_folder, output_filename)

        image.save(output_path)

        print(f"Compressed {filename} saved as {output_filename} in {compressed_folder}")

print("videos compressed to 10x10")

# Get the list of files in the folder
files = natsorted(os.listdir(compressed_folder))

allboards = []

for v, file in enumerate(files):
    img_path = os.path.join(compressed_folder, file)
    img = Image.open(img_path)

    img = img.convert("L")

    width, height = img.size

    fumen = ""

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))

            if pixel < 128:
                fumen += "X"
            else:
                fumen += "_"

    allboards.append(fumen)

writeto = open("allboards.txt", "w")
for board in allboards:
    writeto.write(board + "\n")
writeto.close()

os.system("node encodeallboards.js > outputfumen.txt")
print("Done! check outputfumen.txt")