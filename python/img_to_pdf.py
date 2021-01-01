import img2pdf
import os
from PIL import Image

with open("out.pdf",'wb') as f:
    f.write(img2pdf.convert(sorted([i for i in os.listdir('img') if i.endswith(".png")], key=lambda fname: int(fname.rsplit('.',1)[0]))))