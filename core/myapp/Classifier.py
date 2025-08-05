import os

import cv2
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from tensorflow import keras

class Classification:
    
    def __init__(self):
        self.model = keras.models.load_model(r'C:\Users\HP\Desktop\project\Hand_digits\Models\digits_classifier.keras')

    def preprocess(img):
        file_bytes = np.asarray(bytearray(img.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

        img = cv2.bitwise_not(np.array(img))

        img = cv2.resize(img, (128,128))
        img = img.astype(np.float32)/255.0
        img = np.expand_dims(img, axis=-1)
        img = np.expand_dims(img, axis=0)
        return img
    
    def predict(self, img)-> int | float:

        expected_shape = (1,128,128,1)
        if img.shape != expected_shape:
            return 0, 0
        
        all_scores = self.model.predict(img)
        predicted_number = np.argmax(all_scores)
        accuracy_score = all_scores[0][predicted_number]
        return predicted_number, accuracy_score