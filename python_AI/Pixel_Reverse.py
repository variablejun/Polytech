from google.colab.patches import cv2_imshow
import numpy as np
import cv2
import matplotlib.pyplot as plt
from google.colab import drive

drive.mount('/content/gdrive') 
#영상 불러오기
img1 = cv2.imread('/content/gdrive/My Drive/Image_Processing/girl.jpg')
# BGR채널순서를 RGB채널로 변경
RGB_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) 
output_img = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB) 
# RGB 채널 나누기
R_img1,G_img1,B_img1=cv2.split(RGB_img1)
# 출력 array 생성하고 0으로 초기화, unsigned byte (0~255)로 설정
R_plus=np.zeros((RGB_img1.shape[0],RGB_img1.shape[1]),dtype=np.ubyte)
G_plus=np.zeros((RGB_img1.shape[0],RGB_img1.shape[1]),dtype=np.ubyte)
B_plus=np.zeros((RGB_img1.shape[0],RGB_img1.shape[1]),dtype=np.ubyte)


def saturation(value): #saturation함수로 정의하기
    if(value>255):
       value = 255;
    return value 

#for문을 돌며 픽셀 반전 연산 하기
for h in range(RGB_img1.shape[0]): # shape [0]세로축
  for w in range(RGB_img1.shape[1]):
    R_plus[h,w] = saturation(255-np.int32(R_img1[h,w])) # 255-현재 픽셀값을 하면 색이 반전이 된다.
    G_plus[h,w] = saturation(255-np.int32(G_img1[h,w])) # 현재 픽셀값이 0 이면 255가 될것이고 255면 0이될것이다.
    B_plus[h,w] = saturation(255-np.int32(B_img1[h,w])) # 그렇게 반전이 된다.
    
    
#영상 다시 넣어주기  
output_img[:,:,0] = R_plus
output_img[:,:,1] = G_plus
output_img[:,:,2] = B_plus

#그림을 화면에 출력
plt.figure(figsize=(20,20))# 영상의 크기를 키워주자
plt.subplot(1,2,1)# 1행 3열에서 1번째 열 plt.title("First image")
plt.title("Image1")
plt.imshow(RGB_img1)
plt.axis("off")
plt.subplot(1,2,2)# 1행 3열에서 1번째 열 plt.title("First image")
plt.title("Pixel Complement")
plt.axis("off")
plt.imshow(output_img)
plt.show()