__author__ = 'koorosh'
import pickle
import os

dataFile = open('inputFile.txt', 'r')
inputData = pickle.load(dataFile)
print(inputData)

if inputData['solver'][0] == 'PT':
    shapeGeneratorPath = "python Piston_Theory/generateDoubleWedge.py " + \
                 str(inputData['wedgeLength'][0]) + " " + \
                 str(inputData['wedgeThickness'][0])
    os.system(shapeGeneratorPath)
    os.system("python Piston_Theory/main.py")

if inputData['solver'][0] == 'sonicFoam':
    print('openfoam')