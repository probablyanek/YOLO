from ML.ai import count
import cv2
import glob
# Read all the images in the folder IN and store them in a list

for img in glob.glob("IN/*.jpg"):
    # Read the image
    image = cv2.imread(img)
    # Call the count function from ML\ai.py
    count(image)