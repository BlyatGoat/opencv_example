#remove image bg
from rembg import remove
from PIL import Image
import cv2
from google.colab.patches import cv2_imshow

input_path ='IMG_2061.png'
output_path ='op.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)

img = cv2.imread('op.png')
cv2_imshow(img)
