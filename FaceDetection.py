import cv2

"""Cascade classifier object, it will contain the face features"""
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

"""Reading the image"""
img = cv2.imread("C:\\Users\\Akashbhardwaj\\Pictures\\Camera Roll\\giri.jpg", 1)

"""GrayScaling the image"""
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

"""Searching the coordinates of the face"""
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=6)

"""Building the rectangle around the face"""
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w , y+h), (0, 255, 0), 3)
    cv2.putText(img, 'Extra Virgin', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (36, 255, 12), 2)

"""Resizing the image"""
resize_img = cv2.resize(img, (int(img.shape[1]/3), (int(img.shape[0]/3))))

"""Displaying the image"""
cv2.imshow("Giri", resize_img)

"""Closes the windows whenever a key is pressed"""
cv2.waitKey(0)
cv2.destroyAllWindows()