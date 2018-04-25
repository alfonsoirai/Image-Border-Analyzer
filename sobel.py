from PIL import Image
import math
import struct
from scipy import misc
import numpy as np
from Tkinter import Tk
from tkFileDialog import askopenfilename

def rgb_to_int(rgb):
    hexadecimal = struct.pack('BBB',*rgb).encode('hex')
    return int('0x'+hexadecimal,0)


def sobel_convertion(img):
    new_img = np.zeros((image.shape[0], image.shape[1]))
    for rownum in range(len(img)-1): # ignore the edge pixels for simplicity (1 to width-1)
        for colnum in range(len(image[rownum])-1): # ignore edge pixels for simplicity (1 to height-1)

            # initialise Gx to 0 and Gy to 0 for every pixel
            Gx = 0
            Gy = 0

            # top left pixel
            p = img[rownum-1][colnum-1]
            r = p[0]
            g = p[1]
            b = p[2]

            # intensity ranges from 0 to 765 (255 * 3)
            intensity = r + g + b

            # accumulate the value into Gx, and Gy
            Gx += -intensity
            Gy += -intensity

            # remaining left column
            p = p = img[rownum-1][colnum]
            r = p[0]
            g = p[1]
            b = p[2]

            Gx += -2 * (r + g + b)

            p = p = img[rownum-1][colnum+1]
            r = p[0]
            g = p[1]
            b = p[2]

            Gx += -(r + g + b)
            Gy += (r + g + b)

            # middle pixels
            p = p = img[rownum][colnum-1]
            r = p[0]
            g = p[1]
            b = p[2]

            Gy += -2 * (r + g + b)

            p = p = img[rownum][colnum+1]
            r = p[0]
            g = p[1]
            b = p[2]

            Gy += 2 * (r + g + b)

            # right column
            p = p = img[rownum+1][colnum-1]
            r = p[0]
            g = p[1]
            b = p[2]

            Gx += (r + g + b)
            Gy += -(r + g + b)

            p = p = img[rownum+1][colnum]
            r = p[0]
            g = p[1]
            b = p[2]

            Gx += 2 * (r + g + b)

            p = p = img[rownum+1][colnum+1]
            r = p[0]
            g = p[1]
            b = p[2]

            Gx += (r + g + b)
            Gy += (r + g + b)

            # calculate the length of the gradient (Pythagorean theorem)
            length = math.sqrt((Gx * Gx) + (Gy * Gy))

            # normalise the length of gradient to the range 0 to 255
            length = length / 4328 * 255

            length = int(length)

            # draw the length in the edge image
            #newpixel = img.putpixel((length,length,length))
            new_img[rownum][colnum] = rgb_to_int((length,length,length))
    misc.imsave('sobel_result.jpg', new_img)

def weightedAverage(pixel):
    return 0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2]

def black_and_white(image, output_image_path):
    grey = np.zeros((image.shape[0], image.shape[1]))
    
    #Recorre todos los pixeles de la imagen  
    for rownum in range(len(image)):
        for colnum in range(len(image[rownum])):
            grey[rownum][colnum] = weightedAverage(image[rownum][colnum])
    misc.imsave(output_image_path, grey)

if __name__ == '__main__':
    Tk().withdraw()
    input_file = askopenfilename()
    image = misc.imread(input_file)
    black_and_white(image,'bw_result.jpg')
    sobel_convertion(image)