from Tkinter import *
from PIL import Image, ImageTk
from scipy.ndimage import imread
import numpy as np
import sys
import math
import io

class Prewitt:

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
        self.boton = Button(self.panelBotones, text = 'Grey Scale', fg = 'black', command = self.black_and_white)
        self.panel = self.panelBotones.create_window(5,0, anchor = 'nw', window = self.boton)
        self.boton = Button(self.panelBotones, text = 'Roberts Convertion', fg = 'black', command = self.roberts_convertion)
        self.panel = self.panelBotones.create_window(5,30, anchor = 'nw', window = self.boton)
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
    
    def black_and_white(self):
        greyImage = Image.new('L',(self.w, self.h))
        greyPixels = greyImage.load()
        pixels = self.image.load()

        for x in range(self.w):
            for y in range(self.h):
                average = sum(pixels[x,y])/3
                greyPixels[x,y] = average
        greyImage.save('prueba_gris.jpg')
        self.actualImage = greyImage
        self.update_image()

    def roberts_convertion(self):
        image = imread('prueba_gris.jpg')
        xMatrix = np.array([[1, 0],
                            [0, -1]])
        yMatrix = np.array([[0, 1],
                            [-1, 0]])

        prewittImage = np.zeros((image.shape[0]-2, image.shape[1]-2, 3), dtype='uint8')

        for y in range(1, image.shape[0]-1):
            for x in range(1, image.shape[1]-1):
                dx = np.sum(np.multiply(image[y-1:y+1, x-1:x+1], xMatrix))
                dy = np.sum(np.multiply(image[y-1:y+1, x-1:x+1], yMatrix))

                gradient = math.sqrt(dx * dx + dy * dy)
                if gradient > 0 and gradient < 255:
                    gradient = gradient
                elif gradient < 0:
                    gradient = 0
                else:
                    gradient = 0

                prewittImage[y-1][x-2] = gradient

        self.actualImage = Image.fromarray(prewittImage)
        self.update_image()

def main():
    try:
        imagePath = 'prueba.jpg'
    except:
        print "Selecciona una imagen"
        return
    root = Tk()
    conversion = Prewitt(imagePath, root)
    root.title("Roberts Conversion")
    root.mainloop()


if __name__ == "__main__":
    main()