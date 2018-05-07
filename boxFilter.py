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
        self.boton = Button(self.panelBotones, text = 'Box Filter', fg = 'black', command = self.box_filter)
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

    def box_filter(self):
        image = imread('prueba.jpg')
        ##Modify the radius from 2 to 10
        radio = 9

        height = image.shape[0]
        width = image.shape[1]

        boxImage = np.zeros((image.shape[0]-2, image.shape[1]-2))
        if radio == 2:
            for i in np.arange(3, height-3):
                for j in np.arange(3, width-3):        
                    sum = 0
                    for k in np.arange(-1, 1):
                        for l in np.arange(-1, 1):
                            a = image.item(i+k, j+l)
                            sum = sum + a
                    b = int(sum / 4.0)
                    boxImage.itemset((i,j), b)
        elif radio == 3:
            for i in np.arange(3, height-3):
                for j in np.arange(3, width-3):        
                    sum = 0
                    for k in np.arange(-1, 2):
                        for l in np.arange(-1, 2):
                            a = image.item(i+k, j+l)
                            sum = sum + a
                    b = int(sum / 9.0)
                    boxImage.itemset((i,j), b)
        elif radio == 4:
            for i in np.arange(3, height-3):
                for j in np.arange(3, width-3):        
                    sum = 0
                    for k in np.arange(-2, 2):
                        for l in np.arange(-2, 2):
                            a = image.item(i+k, j+l)
                            sum = sum + a
                    b = int(sum / 16.0)
                    boxImage.itemset((i,j), b)
        elif radio == 5:
            for i in np.arange(3, height-3):
                for j in np.arange(3, width-3):        
                    sum = 0
                    for k in np.arange(-2, 3):
                        for l in np.arange(-2, 3):
                            a = image.item(i+k, j+l)
                            sum = sum + a
                    b = int(sum / 25.0)
                    boxImage.itemset((i,j), b)
        elif radio == 6:
            for i in np.arange(3, height-3):
                for j in np.arange(3, width-3):        
                    sum = 0
                    for k in np.arange(-3, 3):
                        for l in np.arange(-3, 3):
                            a = image.item(i+k, j+l)
                            sum = sum + a
                    b = int(sum / 36.0)
                    boxImage.itemset((i,j), b)
        elif radio == 7:
            for i in np.arange(3, height-3):
                for j in np.arange(3, width-3):        
                    sum = 0
                    for k in np.arange(-3, 4):
                        for l in np.arange(-3, 4):
                            a = image.item(i+k, j+l)
                            sum = sum + a
                    b = int(sum / 49.0)
                    boxImage.itemset((i,j), b)
        elif radio == 8:
            for i in np.arange(3, height-3):
                for j in np.arange(3, width-3):        
                    sum = 0
                    for k in np.arange(-3, 4):
                        for l in np.arange(-3, 4):
                            a = image.item(i+k, j+l)
                            sum = sum + a
                    b = int(sum / 64.0)
                    boxImage.itemset((i,j), b)
        elif radio == 9:
            for i in np.arange(3, height-3):
                for j in np.arange(3, width-3):        
                    sum = 0
                    for k in np.arange(-4, 4):
                        for l in np.arange(-4, 4):
                            a = image.item(i+k, j+l)
                            sum = sum + a
                    b = int(sum / 81.0)
                    boxImage.itemset((i,j), b)
        elif radio == 10:
            for i in np.arange(3, height-3):
                for j in np.arange(3, width-3):        
                    sum = 0
                    for k in np.arange(-5, 4):
                        for l in np.arange(-5, 4):
                            a = image.item(i+k, j+l)
                            sum = sum + a
                    b = int(sum / 100.0)
                    boxImage.itemset((i,j), b)
        self.actualImage = Image.fromarray(boxImage)
        self.update_image()
        

def main():
    try:
        imagePath = 'prueba.jpg'
    except:
        print "Selecciona una imagen"
        return
    root = Tk()
    conversion = Sobel(imagePath, root)
    root.title("Box Filter")
    root.mainloop()


if __name__ == "__main__":
    main()