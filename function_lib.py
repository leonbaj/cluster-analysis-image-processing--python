#!/usr/bin/python
#program name: function_lib.py
#YOUR name: Jorge Leon Barreno
#date: July 12, 2021
#program description: This file hold all the functions corrisponding to use driver.py
#compiler version: 3.9.5
#non-standard libraries: URL LIB 3, cImage, csv, random, math
#operating system: Windows 10
'''
importing urllib3 do be able to load text file. poolmanager allows to send request to view. 
'''
import math #to-do sqrt function
import random #for createCentroid function that uses random module
import csv #to read csv file
from cImage import * #to manipulate picture pixels etc. 


#This Function displays and asks the user for input which option to go with. 
def Choice():
    print("[1] Image Processing")
    print("[2] Cluster Analysis")
    print("[0] Exit the Program")

#This function takes pixels in from old image to create graypixels.
def grayPixel(oldPixel):
    intensitysum =oldPixel.getRed() + oldPixel.getGreen() + oldPixel.getBlue()
    aveRGB = intensitysum // 3
    newPixel = Pixel (aveRGB, aveRGB, aveRGB)
    return newPixel

#this function Calls the graypixel function to get the graypixels to display,
#old image and grayscale image. 
def makeGrayScale():
    oldImage = FileImage("sunset.jpg")
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myImageWindow = ImageWin("GrayScale", width * 2, height)
    oldImage.draw(myImageWindow)
    newIm = EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            oldPixel = oldImage.getPixel(col,row)
            newPixel = grayPixel(oldPixel)
            newIm.setPixel(col, row, newPixel)
            
    newIm.setPosition(width + 1, 0)
    newIm.draw(myImageWindow)
    myImageWindow.exitOnClick()

#this function gets the size of the old image to double the size of a new image
def doubleImage(oldImage):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()

    newIm = EmptyImage(oldW * 2, oldH * 2)

    for row in range (oldH):
        for col in range(oldW):
            oldPixel = oldImage.getPixel(col,row)

            newIm.setPixel(2 * col, 2 * row, oldPixel)
            newIm.setPixel(2 * col + 1, 2 * row, oldPixel)
            newIm.setPixel(2 * col, 2 * row + 1, oldPixel)
            newIm.setPixel(2 * col + 1, 2 * row + 1, oldPixel)
    return newIm

#This function calls the double image function to get the double size and
#display it along with the original image. 
def makeDoubleImage():
     oldImage = FileImage("sunset.jpg")
     width = oldImage.getWidth()
     height = oldImage.getHeight()

     myWin = ImageWin("Double Size", width * 2, height * 3)
     oldImage.draw(myWin)

     newImage = doubleImage(oldImage)
     newImage.setPosition(0, oldImage.getHeight() + 1)
     newImage.draw(myWin)

     myWin.exitOnClick()

def euclidD(point1, point2): #points are equal-length lists or tupls.
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) **2
        total = total+diff
    euclidDistance = math.sqrt(total)
    return euclidDistance
    


def readFile(filename): #reads csv file called avg_marathon_times[second]
    with open(filename, "r") as dataFile:
        csvReader = csv.reader(dataFile)
        titles = next(csvReader)
        dataDict = {}
        key = 0

        for aLine in csvReader:
            key = key+1
            A = float(aLine[1])
            B = float(aLine[2])
            dataDict[key] = [A,B]
    return dataDict

def createCentroids(k, dataDict): #creates centriods 
    centroids = []
    centroidCount = 0
    centroidKeys = [] #list of unique keys

    while centroidCount < k:
        rKey = random.randint(1, len(dataDict))
        if rKey  not in centroidKeys:  #if key not already selected
            centroids.append(dataDict[rKey]) #addadd to centroid
            centroidKeys.append(rKey) #add key to selected keys
            centroidCount = centroidCount+1
            
    return centroids

def createClusters(k, centroids, dataDict, repeats): #creates clusters
    for aPass in range(repeats):
        print("****PASS", aPass+1, "****")
        clusters = [] #create list of k empty lists
        for i in range(k):
            clusters.append([])

        for aKey in dataDict: #calculates distance to centroid
            distances = []
            for clusterIndex in range(k):
                dToc = euclidD(dataDict[aKey], centroids[clusterIndex])
                distances.append(dToc)

            minDist = min(distances) #find minimum distance
            index = distances.index(minDist)

            clusters[index].append(aKey) # add to cluster

        dimensions = len(dataDict[1]) #recompute the clusers
        for clusterIndex in range(k):
            sums = [0] * dimensions #init sum for each dimension
            for aKey in clusters [clusterIndex]:
                dataPoints = dataDict[aKey]
                for ind in range(len(dataPoints)): # calculate sums
                    sums[ind] = sums[ind]+ dataPoints[ind]
            for ind in range(len(sums)): #calculate the average
                clusterLen = len(clusters[clusterIndex])
                if clusterLen !=0: #do not divide by 0
                    sums[ind] = sums[ind] / clusterLen
            centroids[clusterIndex] = sums #assign avg to centroids

        for c in clusters: #outputs the clusters
            print("CLUSTER")
            for key in c:
                print(dataDict[key], end = " ")
                print()
    return clusters

#actual function which calls all related cluster function
#to create a cluster analysis
def clusterAnalysis(dataFile): 
    marathonDict = readFile(dataFile)
    marathonCentroids = createCentroids(5, marathonDict)
    marathonClusters = createClusters(5, marathonCentroids, marathonDict,3)
    



