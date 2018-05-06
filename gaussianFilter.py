from Tkinter import *
from PIL import Image, ImageTk
from scipy.ndimage import imread
import numpy as np
import sys
import math
import io

class Sobel:

    def __init__(self, path, root):
        self.imagePath = path
        self.image = self.rgb_conversion()
        self.w, self.h = self.image.size
        self.actualImage = self.image

        self.root = root

        self.display = ImageTk.PhotoImage(self.image)
        self.canvas = Canvas(self.root, width = self.w, height = self.h)
        self.label = Label(self.canvas, image = self.display)
        self.label.image = self.display
        self.label.pack()

        self.panelBotones = Canvas(self.root, width=150, height=self.h)
        self.boton = Button(self.panelBotones, text = 'Gaussian Filter', fg = 'black', command = self.gaussian_filter)
        self.panel = self.panelBotones.create_window(5,0, anchor = 'nw', window = self.boton)
        self.panelBotones.pack(side=LEFT)
        self.canvas.pack()

    def update_image(self):
        display = ImageTk.PhotoImage(self.actualImage)
        self.label.config(image=display)
        self.label.image = display

    def rgb_conversion(self):
        image = Image.open(self.imagePath)
        image = image.convert('RGB')
        return image

    def gaussian_filter(self):
        image = imread('prueba.jpg')

        height = image.shape[0]
        width = image.shape[1]

        gaussMatrix = np.array([[0.023528, 0.033969, 0.038393, 0.033969, 0.023528],
                                [0.033969, 0.049045, 0.055432, 0.049045, 0.033969],
                                [0.038393, 0.055432, 0.062651, 0.055432, 0.038393],
                                [0.033969, 0.049045, 0.055432, 0.049045, 0.033969],
                                [0.023528, 0.033969, 0.038393, 0.033969, 0.023528]])

        gaussImage = np.zeros((image.shape[0]-2, image.shape[1]-2))

        for i in np.arange(2, height-2):
            for j in np.arange(2, width-2):        
                sum = 0
                for k in np.arange(-2, 3):
                    for l in np.arange(-2, 3):
                        a = image.item(i+k, j+l)
                        p = gaussMatrix[2+k, 2+l]
                        sum += (p * a)
                b = sum
                gaussImage.itemset((i,j), b)

        self.actualImage = Image.fromarray(gaussImage)
        self.update_image()

def main():
    try:
        imagePath = 'prueba.jpg'
    except:
        print "Selecciona una imagen"
        return
    root = Tk()
    conversion = Sobel(imagePath, root)
    root.title("Gaussian Filter")
    root.mainloop()


if __name__ == "__main__":
    main()