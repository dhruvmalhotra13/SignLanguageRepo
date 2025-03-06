import cv2
import numpy as np
import os
from pathlib import Path

# Define directory using pathlib (cross-platform support)
directory = Path(__file__).resolve().parent / "archive_3" / "Allsign"
directory = str(directory)  # Convert to string for compatibility with os.listdir()

shape = (2515, 128, 128)
test = np.zeros(shape)
np_ind = 0
flag = True
count = 0

for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    
    img = cv2.imread(file_path)
    
    resized = cv2.resize(img, (128, 128))
    
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    #adjusted = cv2.convertScaleAbs(gray, alpha=2.0, beta=0)
    
    # if(np_ind==62):
    #     cv2.imshow('Image window',gray)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
    #     enhanced=cv2.fastNlMeansDenoising(gray,h=10)
        
    #     cv2.imwrite("test.jpg", enhanced)
    
    test[np_ind] = gray.copy()

    # if(flag==True):
    #     print(test[np_ind])
    #     print("----------------------------")
    #     print(gray)
    #     cv2.imshow("Image window", gray)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
    #     cv2.imshow("Image window", cv2.convertScaleAbs(test[np_ind]))
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
    #     flag=False
        
    np_ind += 1
    count += 1

test = test.astype("uint8")
cv2.imshow("Image window", test[0])
cv2.waitKey(0)
cv2.destroyAllWindows()

np.save('test_sign.npy', test)
load_test = np.load('test_sign.npy')
print(load_test.shape)
