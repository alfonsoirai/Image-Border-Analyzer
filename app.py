from PIL import Image
from scipy import misc
import numpy as np
from Tkinter import Tk
from tkFileDialog import askopenfilename

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