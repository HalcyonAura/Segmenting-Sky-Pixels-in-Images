# This script was used to binarize outputs for use in reports

import os
import sys
import cv2
import numpy as np
import math


camera = os.listdir('.\\CityscapesAll\\')
for c in camera:
        print(c)
        files = os.listdir('.\\CityscapesAll\\' + c)
        if c == '75':
                os.mkdir('.\\CityscapesBinary\\' + c)
                for f in files:
                        #print(f)
                        pred = cv2.imread('.\\CityscapesAll\\' + c + '\\' + f, 1)
                        for i in range(len(pred)):
                                for j in range(len(pred[0])):
                                    if (pred[i][j][0] == 180) and (pred[i][j][1] == 130) and (pred[i][j][2] == 70):
                                    #if (pred[i][j][0] == 0) and (pred[i][j][1] == 0) and (pred[i][j][2] == 255):
                                        pred[i][j][0] = 1
                                        pred[i][j][1] = 1
                                        pred[i][j][2] = 1
                                    else:
                                        pred[i][j][0] = 0
                                        pred[i][j][1] = 0
                                        pred[i][j][2] = 0
                        cv2.imwrite('.\\CityscapesBinary\\'+ c + '\\' + f, pred)
