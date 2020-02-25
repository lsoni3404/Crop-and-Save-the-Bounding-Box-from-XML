import numpy as np # linear algebra
import xml.etree.ElementTree as ET # for parsing XML
from PIL import Image # to read images
import os
import glob
path_annots = '/home/lalitsoni/datasets/Oxford-IIIT-Pets/Annotation'
path_images = '/home/lalitsoni/datasets/Oxford-IIIT-Pets/images'
#automated code
for filename in os.listdir(path_annots):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(path_annots, filename)
    tree = ET.parse(fullname)
    root = tree.getroot()
    # height = int(tree.findtext("./size/height"))
    # width = int(tree.findtext("./size/width"))
    xmin = int(tree.findtext("./object/bndbox/xmin"))
    ymin = int(tree.findtext("./object/bndbox/ymin"))
    xmax = int(tree.findtext("./object/bndbox/xmax"))
    ymax = int(tree.findtext("./object/bndbox/ymax"))
    image_name , extension = os.path.splitext(filename)
    full_image_name = image_name + '.jpg' 
    im = Image.open(r"/home/lalitsoni/datasets/Oxford-IIIT-Pets/images/"+full_image_name) 
    im1 = im.crop((xmin, ymin, xmax, ymax))
    im1.save("/home/lalitsoni/datasets/Oxford-IIIT-Pets/new_images/"+full_image_name)