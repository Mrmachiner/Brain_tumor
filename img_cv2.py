import cv2
image = cv2.imread("/home/minhhoang/Brain_tumor/data_test/yes/Y1.jpg")
cv2.imshow("image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(gray, 145, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("thres", thresh)
cv2.waitKey()
