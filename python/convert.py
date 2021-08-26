""" Python script to converts images in the target folder into a single pdf file """
# https://youtu.be/sD6L9ZpuAzs
import img2pdf
import os
image_folder = '/home/asimcode/images'
os.chdir(image_folder)
pdf_name = "images.pdf"
names = os.listdir()
names.sort()
with open(pdf_name,"wb") as f:
    imgs= []
    for file_name in names:
        path = os.path.join(image_folder,file_name)
        imgs.append(path)
    f.write(img2pdf.convert(imgs))
