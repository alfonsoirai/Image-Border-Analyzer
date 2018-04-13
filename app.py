from PIL import Image
from Tkinter import Tk
from tkFileDialog import askopenfilename

def black_and_white(input_image_path, output_image_path):
    color_image = Image.open(input_image_path)
    bw = color_image.convert('L')
    bw.save(output_image_path)

if __name__ == '__main__':
    Tk().withdraw()
    input_file = askopenfilename()
    black_and_white(input_file,'bw_result.jpg')