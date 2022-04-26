
import numpy as np
import cv2
import matplotlib.pyplot as plt
 
#영상 불러오기
img1 = cv2.imread('../Image_Processing/girl.jpg')
# BGR채널순서를 RGB채널로 변경
RGB_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) 
output_img = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB) 
# RGB 채널 나누기
R_img1,G_img1,B_img1=cv2.split(RGB_img1)

# 출력 array 생성하고 0으로 초기화, unsigned byte (0~255)로 설정
R_plus=np.zeros((RGB_img1.shape[0],RGB_img1.shape[1]),dtype=np.ubyte)
G_plus=np.zeros((RGB_img1.shape[0],RGB_img1.shape[1]),dtype=np.ubyte)
B_plus=np.zeros((RGB_img1.shape[0],RGB_img1.shape[1]),dtype=np.ubyte)
C=5.0  #곱하기 상수값
def saturation(value): #saturation함수로 정의하기
    if(value>255):
       value = 255;
    return value 
#for문을 돌며 픽셀 곱하기 연산 하기
for h in range(RGB_img1.shape[0]):
  for w in range(RGB_img1.shape[1]):
    R_plus[h,w] = saturation(np.int32(R_img1[h,w])*C) # 미리 정의 해놓은 상수로 곱한다. saturation, wrapping, minmax로 오버플로우 처리한다.
    G_plus[h,w] = saturation(np.int32(G_img1[h,w])*C) 
    B_plus[h,w] = saturation(np.int32(B_img1[h,w])*C) 

#그림을 화면에 출력
plt.figure(figsize=(20,20))# 영상의 크기를 키워주자
plt.subplot(1,2,1)# 1행 3열에서 1번째 열 plt.title("First image")
plt.title("Image1")
plt.imshow(RGB_img1)
plt.axis("off")
plt.subplot(1,2,2)# 1행 3열에서 2번째 열
output_img[:,:,0]=R_plus
output_img[:,:,1]=G_plus
output_img[:,:,2]=B_plus
plt.title("Multiplication image")
plt.imshow(output_img)
plt.axis("off")
plt.show()