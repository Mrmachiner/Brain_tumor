import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2
import imutils
import numpy as np
import matplotlib.pyplot as plt
import time

class Predict():
    def crop_brain_contour(self, image, plot=False):
        
        #import imutils
        #import cv2
        #from matplotlib import pyplot as plt
        # Convert the image to grayscale, and blur it slightly
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)

        # Threshold the image, then perform a series of erosions +
        # dilations to remove any small regions of noise
        thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.erode(thresh, None, iterations=2)
        thresh = cv2.dilate(thresh, None, iterations=2)

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
        
        return new_image
    def predict_img(self, path_img='../../brain_tumor_dataset/yes/Y1.jpg', best_model=None):
        img_test = cv2.imread(path_img)
        img_test = self.crop_brain_contour(img_test)
        img_test = cv2.resize(img_test, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)
        img_test = tf.cast(img_test, tf.float32)
        a = []
        a.append(img_test)
        a = np.array(a)
        start = time.time()
        y_test_prob = best_model.predict(a)
        process_time = time.time() - start
        return y_test_prob, process_time

if __name__ == "__main__":
    best_model = load_model(filepath='models/cnn-parameters-improvement-23-0.91.model')
    img_test = cv2.imread("/home/minhhoang/Brain_tumor/brain_tumor_dataset/yes/Y26.jpg")
    cv2.imshow("img_test",img_test)
    cv2.waitKey()
    cv2.destroyAllWindows()
    img_test = crop_brain_contour(img_test)
    img_test = cv2.resize(img_test, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)
    img_test = tf.cast(img_test, tf.float32)
    a = []
    a.append(img_test)
    a = np.array(a)
    print(img_test.shape)
    start = time.time()
    y_test_prob = best_model.predict(a)
    print("Processing time:", time.time() - start)
    print(y_test_prob)