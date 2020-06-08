import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2
import imutils
import numpy as np
import matplotlib.pyplot as plt
import time
import os


class Predict():
    
    def __init__(self):
        start = time.time()
        self.best_model = load_model(filepath='/home/minhhoang/Brain_tumor/Brain-Tumor-Detection/models/cnn-parameters-improvement-23-0.91.model')
        process_time = time.time() - start
        print("load model", process_time)
    def crop_brain_contour(self, image, plot=False):
        lst_img = []
        #import imutils
        #import cv2
        #from matplotlib import pyplot as plt
        # Convert the image to grayscale, and blur it slightly
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        lst_img.append(gray)

        # Threshold the image, then perform a series of erosions +
        # dilations to remove any small regions of noise
        thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]
        lst_img.append(thresh)
        #cv2.imshow("thresh", thresh)
        thresh = cv2.erode(thresh, None, iterations=2)
        thresh = cv2.dilate(thresh, None, iterations=2)
        #cv2.imshow("erode and dilate", thresh)

        # Find contours in thresholded image, then grab the largest one
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = max(cnts, key=cv2.contourArea)
        

        # Find the extreme points
        extLeft = tuple(c[c[:, :, 0].argmin()][0])
        extRight = tuple(c[c[:, :, 0].argmax()][0])
        extTop = tuple(c[c[:, :, 1].argmin()][0])
        extBot = tuple(c[c[:, :, 1].argmax()][0])
        
        # crop new image out of the original image using the four extreme points (left, right, top, bottom)
        new_image = image[extTop[1]:extBot[1], extLeft[0]:extRight[0]] 
        lst_img.append(new_image)           
        #cv2.imshow("crop", new_image)
        if plot:
            plt.figure()

            plt.subplot(1, 2, 1)
            plt.imshow(image)
            
            plt.tick_params(axis='both', which='both', 
                            top=False, bottom=False, left=False, right=False,
                            labelbottom=False, labeltop=False, labelleft=False, labelright=False)
            
            plt.title('Original Image')
                
            plt.subplot(1, 2, 2)
            #plt.imshow(new_image)

            plt.tick_params(axis='both', which='both', 
                            top=False, bottom=False, left=False, right=False,
                            labelbottom=False, labeltop=False, labelleft=False, labelright=False)

            plt.title('Cropped Image')
            
            #plt.show()
        
        return new_image, lst_img
    def predict_img(self, path_img='/home/minhhoang/Brain_tumor/data_test/yes/Y1.jpg'):
        img_test = cv2.imread(path_img)
        img_test, lst_img = self.crop_brain_contour(img_test)
        img_test = cv2.resize(img_test, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)
        lst_img.append(img_test)
        img_test = img_test.astype(np.float64)
        # img_test = tf.cast(img_test, tf.float32)
        print(img_test.shape)
        a = []
        a.append(img_test)
        a = np.array(a)

        start = time.time()
        y_test_prob = self.best_model.predict(a)
        process_time = time.time() - start
        return y_test_prob, process_time, lst_img

if __name__ == "__main__":
    predict = Predict()
    # path_model = '/home/minhhoang/Brain_tumor/Brain-Tumor-Detection/models/cnn-parameters-improvement-23-0.91.model'
    # best_model = load_model(filepath=path_model)
    check, time, lst_img = predict.predict_img()
    print(check)
    print(time)
    if check[0][0]==1:
        print("sida")
    for img in lst_img:
        cv2.imshow("jpg", img)
        cv2.imwrite("abcd.jpg", img)
        cv2.waitKey()
        cv2.destroyAllWindows()