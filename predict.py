import cv2
from keras.preprocessing.image import load_img
import numpy as np
import matplotlib.pyplot as plt
import os

from google.colab import drive
drive.mount('/content/drive')

test_dst = os.listdir('/content/drive/My Drive/Potholes Dataset/Test/')

def predict():

    for testimg in test_dst:
      # load the image
      img = os.path.join(test_path,testimg)
      img12 = cv2.imread(img,cv2.IMREAD_COLOR)
      # resizing the image
      img12 = cv2.resize(img12,(224,224))
      plt.figure()
      plt.imshow(img12) 
      plt.show()
      img11 = np.array(img12)
      img11 = np.expand_dims(img11,axis = 0)

      test_result = np.round(model.predict(img11))
      
      if test_result[0][0] == 1 :
        print("Road with no potholes")
      else:
        print("Road with potholes")
        
if __name__ == '__main__':
    predict()