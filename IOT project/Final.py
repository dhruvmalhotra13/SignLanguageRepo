import os
import cv2
import numpy as np
import tensorflow as tf
import joblib
from pathlib import Path

# Define cross-platform paths
base_dir = Path(__file__).resolve().parent  # Gets the script's directory

encoder_path = base_dir / "Autoencoder" / "autoencoder_2.keras"
cluster_path = base_dir / "Autoencoder" / "cluster_2.joblib"

shape = (1, 128, 128)
test = np.zeros(shape)

def show_image(image):
    cv2.imshow("Saved", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def make_test(img):
    grayed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    show_image(grayed_img)
    
    _, mask = cv2.threshold(grayed_img, 90, 255, cv2.THRESH_BINARY)
    final_img = cv2.bitwise_and(grayed_img, grayed_img, mask=mask)
    show_image(final_img)
    
    final_img = final_img.astype('float32') / 255
    show_image(final_img)
    
    test[0] = final_img
    predict(test)

def predict(img):
    latent = encoder.predict(img)
    flattened = latent.reshape(len(latent), -1)
    outcome = cluster.predict(flattened)
    print(outcome)

# Load models using cross-platform paths
encoder = tf.keras.models.load_model(str(encoder_path))
cluster = joblib.load(str(cluster_path))

# Camera setup
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 128)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 128)

while True:
    ret, img = cam.read()
    cv2.imshow('Preview', img)
    
    key_press = cv2.waitKey(1) & 0xFF
    if key_press == ord(' '):
        cv2.destroyAllWindows()
        make_test(cv2.resize(img, (128, 128)))
    elif key_press == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
