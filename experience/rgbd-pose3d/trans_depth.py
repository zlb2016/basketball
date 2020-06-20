import cv2
import os.path
import glob
import numpy as np
from PIL import Image
 
def convertPNG(pngfile,outdir):
    # READ THE DEPTH
    im_depth = cv2.imread(pngfile)
    #apply colormap on deoth image(image must be converted to 8-bit per pixel first)
    im_color=cv2.applyColorMap(cv2.convertScaleAbs(im_depth,alpha=15),cv2.COLORMAP_HSV)
    #convert to mat png
    im=Image.fromarray(im_color)
    #save image
    im.save(os.path.join(outdir,os.path.basename(pngfile)))
if __name__ == "__main__":
    # for pngfile in glob.glob("PNG FILE"):#C:/Users/BAMBOO/Desktop/source pics/rgbd_6/depth/*.png
    #     convertPNG(pngfile,"TARGET FILE")#C:/Users/BAMBOO/Desktop/source pics/rgbd_6/color
    convertPNG('./test_63.png',"depth_rgb")
    print('done')
    pass 
