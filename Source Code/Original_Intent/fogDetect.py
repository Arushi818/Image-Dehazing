import cv2
import sys
import math
import os 
import numpy as np

#https://www.mdpi.com/2073-4433/14/7/1125

def main():
    image = input("Enter your image here: ")

def calculate2DDirectionalEntropy(image):
    ddepth = cv2.CV_32F

    dx = cv2.Sobel(image, ddepth, 1, 0)
    dy = cv2.Sobel(image, ddepth, 0, 1)

    grad45 = cv2.Sobel(image, ddepth, 1, 1,) #ksize=3)
    grad135 = cv2.Sobel(image, ddepth, 1, -1,)# ksize=3)

    gradMagStraight = getGradMag(dx,dy)
    theta1 = getDirectionEdgePts(dx,dy)

    gradMagDiag = getGradMag(grad45,grad135)
    theta2 = getDirectionEdgePts(grad45,grad135)


def discretize_direction(direction, n):

    quantized_direction = np.floor((360 / n) * direction) + 1
    return quantized_direction.astype(int)


def getGradMag(dx,dy):

    mag = cv2.magnitude(dx,dy)

    return mag

def getDirectionEdgePts(dx,dy):

    theta = math.degrees(math.atan2(dx/dy))+180

    return theta



#function to calculate 2d Gray scale entropy of the image
#@param image the image whose grayscale entropy is to be calculated
#@return the grayscale entropy value of the image
def calculate2DGrayscaleEntropy(image):
    countRes = 0
    for x1 in range(255):
        count = 0
        for x2 in range(255):
            px1x2 = probX1andX2(image, x1,x2)
            count += px1x2 * math.log2(px1x2)
        countRes+= count
    
    return -countRes

#function to calculate probability of a pixel with intensity x1 another one with intensity x2 to occur
#@param image, the image being processed
#@x1 first intensity
# @x2 second intensity
# @return the probability of the tuple occuring 
def probX1andX2(image, x1,x2):
    count = 0
    for row in range(image.shape[1]):
        for col in range(image.shape[0]):
            neighbouravg = findNeighbourAvg(image, row,col)
            if(image[row][col] == x1 and x2 == neighbouravg):
                count +=1

    N = image.shape[1] * image.shape[0]
    return count/N

#function to find average intensity of the 8 neighbours of a pixel at a given row and column
#@param image, the image to be explored
#@row, the row location of the pixel
#@column, the column location of the pixel
#@return the average pixel intensity of the neighbourhood
def findNeighbourAvg(image, row, col):
    sum = 0
    count = 0
    for x in range(row-1,row+2):
        for y in range(col-1,col+2):
            sum += image[x][y]
            count+=1

    return sum/count

#function to perform canny edge detection
#@param image, the image on which edge detection is to be performed
#@return canny, the image resulting from canny edge detection
def performEdgeDetection(image):
    grayImg = convertToGrayScale(image)
    canny = cv2.Canny(grayImg, 100,200)

    return canny 
   
#function to convert image to grayscale
#@param image, the image to be converted
#@return the gray scale image 
def convertToGrayScale(image):
    grayscaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return grayscaleImage


#function to read image as a grayscale
#@param path, string, the path where the image to be read is located
def readImage(path):
    image = cv2.imread(path)
    if image is None: 
        print("Error: invalid image name")
        return
    return image

#function to save picture
#@param filename, string
#@param imageObj, an image
#@param, dirPath, string, the path directorty where the file is to be saved
def saveImage(filename, imageObj, dirPath):
    os.chdir(dirPath)
    cv2.imwrite(filename,imageObj)

#function to display an image 
#@param imageObj, the image to display
def display(imageObj):  
    cv2.imshow('Image', imageObj)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

#function to display 2 images 
#@param image1Path, the path to the image to display
#@param image2Path, the path to the image to display
def  display2images(image1Path, image2Path):
    image1 = cv2.imread(image1Path)
    image2 = cv2.imread(image2Path,cv2.IMREAD_GRAYSCALE)

    cv2.namedWindow(image1Path, cv2.WINDOW_NORMAL) 
    cv2.namedWindow(image2Path, cv2.WINDOW_NORMAL)

    cv2.imshow(image1Path, image1)
    cv2.imshow(image2Path, image2)

    cv2.waitKey(5000)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
