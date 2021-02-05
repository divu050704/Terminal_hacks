# install pip via command - sudo apt install pip3
# install cv2 via command - pip3 install opencv-python
import cv2 

# Save image in set directory 
# Read RGB image 
img = cv2.imread('Enter_the_file_name)  
  
# Output img with window name as 'image' 
cv2.imshow('image', img)  
  
# Maintain output window utill 
# user presses a key 
cv2.waitKey(0)         
  
# Destroying present windows on screen 
cv2.destroyAllWindows()  
# Save this file in folder where your images are situated
