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
# RGB 채널 나누기
R_img,G_img,B_img=cv2.split(RGB_img)

# Y, I, Q_img파일 생성하고 0으로 초기화
Y_img=np.zeros((RGB_img.shape[0],RGB_img.shape[1]),dtype=np.float64)
# 0으로 채워진 float64 타입의 2차원 배열을 반환해준다
# 512,512 의 배열크기
I_img=np.zeros((RGB_img.shape[0],RGB_img.shape[1]),dtype=np.float64)
Q_img=np.zeros((RGB_img.shape[0],RGB_img.shape[1]),dtype=np.float64)

#for문을 돌며 픽셀값 계산하기
for h in range(RGB_img.shape[0]):#512 가로
  for w in range(RGB_img.shape[1]):#512 세로
    Y_img[h,w]=0.299*R_img[h,w]+0.587*G_img[h,w]+0.114*B_img[h,w] #표기된 공식에 따라서 계산을 반복한다
    I_img[h,w]=0.596*R_img[h,w]-0.275*G_img[h,w]-0.321*B_img[h,w]
    Q_img[h,w]=0.212*R_img[h,w]-0.523*G_img[h,w]+0.311*B_img[h,w]
#그림을 화면에 출력
plt.figure(figsize=(20,20))# 영상의 크기를 키워주자
plt.subplot(1,4,1)# 1행 4열에서 1번째 열 plt.title("First image")
plt.title("Original Image")
plt.imshow(RGB_img)
plt.axis("off")
plt.subplot(1,4,2)# 1행 4열에서 2번째 열
RGB_img[:,:,0]=Y_img
RGB_img[:,:,1]=Y_img
RGB_img[:,:,2]=Y_img
plt.title("Y Channel")
plt.imshow(RGB_img)
plt.axis("off")
plt.subplot(1,4,3)# 1행 4열에서 3번째 열
RGB_img[:,:,0]=I_img
RGB_img[:,:,1]=I_img
RGB_img[:,:,2]=I_img
plt.title("I Channel")
plt.imshow(RGB_img)
plt.axis("off")
plt.subplot(1,4,4)# 1행 4열에서 4번째 열
RGB_img[:,:,0]=Q_img
RGB_img[:,:,1]=Q_img
RGB_img[:,:,2]=Q_img
plt.title("Q Channel")
plt.imshow(RGB_img)
plt.axis("off")
plt.show()