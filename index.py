import cv2 
import numpy as np 

def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply GaussianBlur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Apply Canny
    edges = cv2.Canny(blur, 50, 150) 
    
    return edges

def blur_image(image):
    # Apply GaussianBlur
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    
    black_white = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    
    return black_white

image_original = cv2.imread('gambar.png')

image_processed = preprocess_image(image_original)

image_blur = blur_image(image_original)

cv2.imshow('Original gambar', image_original)
cv2.imshow('Processed gambar', image_processed)
cv2.imshow('Blur gambar', image_blur)
cv2.waitKey(0)