import cv2
import matplotlib.pyplot as plt
from PIL import Image
import os

from dataclasses import dataclass
@dataclass
class Pixel:
    r : int
    g : int
    b : int

@dataclass
class ImagePPM:
    width:int
    height:int
    pixels:list[Pixel]


def showImageFromPath(path):
    img = cv2.imread(path)
    # Remember, opencv by default reads images in BGR rather than RGB
    # So we fix that by the following
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imwrite(".temp.png",img) 
    img2 = Image.open(".temp.png")
    img2.show()
    os.remove(".temp.png") 

def showImage(imgppm):
    saveImage(imgppm, '.temp.ppm')
    img = cv2.imread('.temp.ppm')
    # Remember, opencv by default reads images in BGR rather than RGB
    # So we fix that by the following
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imwrite(".temp.png",img) 
    img2 = Image.open(".temp.png")
    img2.show()
    os.remove(".temp.png") 
    os.remove('.temp.ppm')

def loadImage(path):
    allPixels = []
    f = open(path, "r")
    allLines= f.readlines()
    usefullLines = []
    for line in allLines:
        if line.startswith('#') or len(line)==0:
            None
        else:
            usefullLines.append(line)

    usefullLines = usefullLines[1:]
    dimensionsAndPixels=[]

    for line in usefullLines:
        for w in line.split():
            dimensionsAndPixels.append(w)

    width: int = int(dimensionsAndPixels[0])
    height: int = int(dimensionsAndPixels[1])
    for i in range(3,len(dimensionsAndPixels)-1,3):
        allPixels.append(Pixel(int(dimensionsAndPixels[i]),int(dimensionsAndPixels[i+1]),int(dimensionsAndPixels[i+2])))
    return ImagePPM(width, height ,allPixels)



def saveImage(img,path):
    f = open(path, "w")
    f.write("P3\n")
    f.write("#created by my wonderfull app !\n")
    f.write(f'{img.width} {img.height} 255\n')
    for i in range(0,len(img.pixels)):
        f.write(f'{img.pixels[i].r}\n{img.pixels[i].g}\n{img.pixels[i].b}\n')




def display2DPoints(*lstPoints: list):
    '''This function takes a list of Point2D as parameter and plot them by using the matplotlib module'''
    for lstPoint in lstPoints:
        xSet: list =[]
        ySet: list = []
        for p in lstPoint:
            xSet = xSet + [p.x]
            ySet = ySet + [p.y]    
        plt.plot(xSet, ySet, marker='.')
    plt.show()
