from PIL import ImageGrab
import numpy as np
import cv2



def snap_grab():
    img = ImageGrab.grab(bbox=(0,47,641,527))
    img = img.resize((256,256))
    img = np.array(img)
   # print(str(img.size))
    return img
