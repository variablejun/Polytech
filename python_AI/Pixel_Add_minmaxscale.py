from google.colab.patches import cv2_imshow
import numpy as np
import cv2
import matplotlib.pyplot as plt

from google.colab import drive

drive.mount('/content/gdrive') 
#영상 불러오기
img1 = cv2.imread('/content/gdrive/My Drive/Image_Processing/aero2.bmp')
img2 = cv2.imread('/content/gdrive/My Drive/Image_Processing/milkdrop.bmp')
# BGR채널순서를 RGB채널로 변경
RGB_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) 
RGB_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB) 
output_img = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) 
# RGB 채널 나누기
R_img1,G_img1,B_img1=cv2.split(RGB_img1)
R_img2,G_img2,B_img2=cv2.split(RGB_img2)
#  0으로 초기화
R_plus = np.zeros((RGB_img1.shape[0],RGB_img1.shape[1]),dtype=np.ubyte)
G_plus = np.zeros((RGB_img1.shape[0],RGB_img1.shape[1]),dtype=np.ubyte)
B_plus = np.zeros((RGB_img1.shape[0],RGB_img1.shape[1]),dtype=np.ubyte)

min = 0.0
max = 255.0

for h in range (RGB_img1.shape[0]):
  for w in range (RGB_img1.shape[1]):
    r= np.int32(R_img1[h,w])+np.int32(R_img2[h,w])
    if(r > 255):
      R_plus[h,w] = (r-min)/(max-min) * max # 넘치는 값을 미리정규화된 값으로 0~255 사이로 재계산
    else:
      R_plus[h,w] = r
    g= np.int32(G_img1[h,w])+np.int32(G_img2[h,w])
    if(g > 255):
      G_plus[h,w] = (g-min)/(max-min) * max
    else:
      G_plus[h,w] = g
    b= np.int32(B_img1[h,w])+np.int32(B_img2[h,w])
    if(b > 255):
      B_plus[h,w] = (b-min)/(max-min) * max
    else:
      B_plus[h,w] = b
  
#그림을 화면에 출력
plt.figure(figsize = (20,20)) # 영상의 크기를 키워주자
plt.subplot(1, 3, 1) # 1행 4열에서 1번째 열 plt.title("First image")
plt.title("Image1")
plt.imshow(RGB_img1)
plt.axis("off")
plt.subplot(1, 3, 2) # 1행 4열에서 2번째 열
plt.title("Image2")
plt.imshow(RGB_img2)
plt.axis("off")
plt.subplot(1, 3, 3) # 1행 4열에서 3번째 열
output_img[:,:,0] = R_plus
output_img[:,:,1] = G_plus
output_img[:,:,2] = B_plus
plt.title("Added Image")
plt.imshow(output_img)
plt.axis("off")
plt.show()