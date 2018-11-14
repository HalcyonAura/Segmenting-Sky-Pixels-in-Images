#To use:
#This is how my file structure for testing was set up
#./CameraNumber/*.png (all the output images from the model for this specific camera)
#./CameraNumber.png (the segmentation image)
#ouput: ./CameraNumber.txt

#e.g. Running test on Camera 204
#run the program (py 2.7 I think, if not try 3.x)
#use arguments to run the script IE: python iou.py 'CameraNumberOnly' e.g. python iou.py '204'
#As it runs it will output the image it is currently analyzing
#It will end with a text file (CameraNumber.txt) to your current directory.
#Scroll to the bottom of the file to find MCR, mIOU, etc.

import os
import sys
import cv2
import numpy as np
import math

camera = sys.argv[1]
files = os.listdir('.\\Cam' + camera + '\\')
maskFile = '.\\' + camera + '.png'
text = open('Camera' + camera + '.txt', 'w+')
text.write(camera)
aveIOU = 0
avePrec = 0
aveRec = 0
aveMCR = 0
for file in files:
    print (file)
    pred = cv2.imread('.\\Cam' + camera + '\\' + file, 1)
    mask = cv2.imread(maskFile, 1)
    iou = np.zeros([len(mask),len(mask[0])])
    fileSum = 0
    for i in range(len(mask)):
        for j in range(len(mask[0])):
            #This color correlates to matlab's output for the sky in our RefineNet model
            if (pred[i][j][0] == 0) and (pred[i][j][1] == 0) and (pred[i][j][2] == 128) and (mask[i][j][0] == 255):
                fileSum+=1
                iou[i][j] = 1
            elif (pred[i][j][0] == 0) and (pred[i][j][1] == 0) and (pred[i][j][2] == 128):
                    fileSum+=1

            #This is if you're running the model trained on cityscapes that outputs a multitude of colors
            #the color specified signifies sky in the matlab model
            #if (pred[i][j][0] == 180) and (pred[i][j][1] == 130) and (pred[i][j][2] == 70) and (mask[i][j][0] == 255):
            #    fileSum+=1
            #    iou[i][j] = 1
            #elif (pred[i][j][0] == 180) and (pred[i][j][1] == 130) and (pred[i][j][2] == 70):
            #        fileSum+=1
    TP = np.sum(iou)
    FN = np.sum(mask)/765 - TP  #255*3
    FP = fileSum - TP
#    print(mask ', np.sum(mask/255/3))
#    print('filesum ', fileSum)
#    print('TP ', TP)
#    print('TN ' ,TN)
#    print('FP ', FP)
    iou = (TP/(TP+FP+FN))
    precision = (TP/(TP+FP))
    if math.isnan(precision):
        precision = 0.0
    recall = (TP/(TP+FN))
    MCR = (FP+FN)/(len(mask)*len(mask[0]))
    aveIOU += iou
    avePrec += precision
    aveRec += recall
    aveMCR += MCR
    text.write('\n' + file + ' IOU: ' + str(iou) + ' Precision: ' + str(precision) + ' Recall: ' + str(recall) + ' MCR: ' + str(MCR))


text.write('\nAverage IOU: ' + str(aveIOU/len(files)) + '\nAverage Precision: ' + str(avePrec/len(files)) + '\nAverage Recall: ' + str(aveRec/len(files)) + '\nAverage MCR: ' + str(aveMCR/len(files)))
text.close()
