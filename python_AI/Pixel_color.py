from google.colab.patches import cv2_imshow
import numpy as np
import cv2
import matplotlib.pyplot as plt

from google.colab import drive

drive.mount('/content/gdrive') 
#영상 불러오기
origin_img = cv2.imread('/content/gdrive/My Drive/Image_Processing/lena.jpg')

# BGR채널순서를 RGB채널로 변경
RGB_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2RGB)
# R,G,B 채널로 분할하기 
Red_img, Green_img, Blue_img = cv2.split(RGB_img) # 채널을 분리 시키고 RGB순서대로 대입
#그림을 화면에 출력
#분리한것은 원본의 빨간색, 초록색, 파란색의 영역을 나누엇다고 봐도된다,
#아리 코드에서 2번에 Red_img를 주면 원본에 파란색영역이 빨간색으로 칠해진다.

#YCrCb_img = cv2.cvtColor(RGB_img, cv2.COLOR_RGB2YCrCb) RGB순서로 바꿔주고 그것을 다른 색상모델로 바꾸어준것
#YCrCb_img = cv2.cvtColor(RGB_img, cv2.COLOR_RGB2HSV)
plt.subplot(1, 4, 1) # 1행 4열에서 1번째 열 
#원 영상 출력
plt.title("Original Image")
plt.imshow(RGB_img)
# R채널만 출력
RGB_img[:,:,0] = Red_img # 분리된 3개의 채널, 각 자리는 위에서 컨버트로 인해 BGR->RGB가 되어 만약 여기만 주면 빨간색나옴
RGB_img[:,:,1] = Red_img # R0 G1 B2 를 의미한다
RGB_img[:,:,2] = Red_img

plt.subplot(1, 4, 2) # 1행 4열에서 2번째 열
plt.title("Red Channel")
plt.imshow(RGB_img) # 회색이 나온다.

# G 채널만 출력
RGB_img[:,:,0] = Green_img
RGB_img[:,:,1] = Green_img # 여기만 채우면 초록색이 나온다 
RGB_img[:,:,2] = Green_img

plt.subplot(1, 4, 3) # 1행 4열에서 3번째 열
plt.title("Green Channel")
plt.imshow(RGB_img)
# B 채널만 출력
RGB_img[:,:,0] = Blue_img
RGB_img[:,:,1] = Blue_img
RGB_img[:,:,2] = Blue_img

plt.subplot(1, 4, 4) # 1행 4열에서 4번째 열
plt.title("Blue Channel")
plt.imshow(RGB_img)

plt.show()