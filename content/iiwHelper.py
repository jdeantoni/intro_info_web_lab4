import cv2
import matplotlib.pyplot as plt
from PIL import Image
import os


def showImage(path):
    img = cv2.imread(path)
    # Remember, opencv by default reads images in BGR rather than RGB
    # So we fix that by the following
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imwrite(".temp.png",img) 
    img2 = Image.open(".temp.png")
    img2.show()
    os.remove(".temp.png") 
    

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


    height=dimensionsAndPixels[0]
    width=dimensionsAndPixels[1]
    for i in range(3,len(dimensionsAndPixels)-1,3):
        allPixels.append(Pixel(dimensionsAndPixels[i],dimensionsAndPixels[i+1],dimensionsAndPixels[i+2]))
    return Image(height,width,allPixels)



def saveImage(img,path):
    f = open(path, "w")
    f.write("P3\n")
    f.write("#created by my wonderfull app !\n")
    f.write(f'{img.height} {img.width} 255\n')
    for i in range(3,len(img.pixels)-1,3):
        f.write(img.pixels[i],img.pixels[i+1],img.pixels[i+2],"\n")




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
