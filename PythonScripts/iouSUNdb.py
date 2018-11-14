import os
import numpy as np
import cv2
import math

testFiles = ['F1', 'I1'] #Referring to the folder containing finetune split 1 results, and the folder containing trained from scratch split 1 results
for cam in testFiles:
    print (cam)
    aveIOU = 0
    avePrec = 0
    aveRec = 0
    aveMCR = 0
    text = open('SUNdb_' + cam + '.txt', 'w+')
    text.write(str(cam))
    listFiles = os.listdir('./SUNdb/SUNdbTest/SUNdb_'+cam+'/predict_result_mask/')
    for f in listFiles:
        segImgPath = './SUNdb/TestSegImages/' + f[:-3] + '.png'
        segImg = cv2.imread(segImgPath,1)
        testImgPath = './SUNdb/SUNdbTest/SUNdb_' + str(cam) + '/predict_result_mask/' + f
        testImg = cv2.imread(testImgPath,1)
        
        fileSum = 0
        iou = np.zeros([len(segImg),len(segImg[0])])
        
        for i in range(len(segImg)):
            for j in range(len(segImg[0])):
            #This color correlates to matlab's output for the sky in our RefineNet model
                if (testImg[i][j][0] == 0) and (testImg[i][j][1] == 0) and (testImg[i][j][2] == 128) and (segImg[i][j][0] == 1):
                    fileSum+=1
                    iou[i][j] = 1
                elif (testImg[i][j][0] == 0) and (testImg[i][j][1] == 0) and (testImg[i][j][2] == 128):
                    fileSum+=1

        TP = np.sum(iou)
        FN = np.sum(segImg)/3 - TP  #255*3 if 3 dim image... not sure what this image is though if vals not at 1 and 0
        FP = fileSum - TP

        iou = (TP/(TP+FP+FN))
        precision = (TP/(TP+FP))
        if math.isnan(precision):
            precision = 0.0
        if math.isnan(iou):
            iou = 0.0
        recall = (TP/(TP+FN))
        MCR = (FP+FN)/(len(segImg)*len(segImg[0]))
        aveIOU += iou
        avePrec += precision
        aveRec += recall
        aveMCR += MCR
        text.write('\n' + f + ' IOU: ' + str(iou) + ' Precision: ' + str(precision) + ' Recall: ' + str(recall) + ' MCR: ' + str(MCR))
    text.write('\nAverage IOU: ' + str(aveIOU/len(listFiles)) + '\nAverage Precision: ' + str(avePrec/len(listFiles)) + '\nAverage Recall: ' + str(aveRec/len(listFiles)) + '\nAverage MCR: ' + str(aveMCR/len(listFiles)))
    text.close()
