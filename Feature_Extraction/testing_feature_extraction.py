# testing feature extraction

import cv2
from skimage.filters.rank import entropy
from skimage.morphology import disk
from scipy import ndimage as nd
from skimage.filters import sobel
import pandas as pd

img = cv2.imread('testDataSet/frame5.jpg')
# cv2.imshow("TEST", img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img2 = img.reshape(-1)

df = pd.DataFrame()
df['Original Pixel Values'] = img2

gaussian_img = nd.gaussian_filter(img, sigma = 3)
gaussian_img1 = nd.gaussian_filter(img, sigma = 2)
gaussian1 = gaussian_img.reshape(-1)
df['Gaussian'] = gaussian1
# cv2.imshow("guassian1", gaussian_img)
# cv2.imshow("guassian2", gaussian_img1)

sobel_img = sobel(img)
gaussian_img = sobel(gaussian_img)
gaussian_img1 = sobel(gaussian_img1)

sobel1 = sobel_img.reshape(-1)
df['sobel'] = sobel1
cv2.imshow("img", img)

img = cv2.GaussianBlur(img, (3,3), cv2.BORDER_DEFAULT)


canny = cv2.Canny(img, 125, 175)
cv2.imshow('Canny  Edges', canny)

coutours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(f'{len(coutours)} contours found')

print(df)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey()
cv2.destroyAllWindows()
