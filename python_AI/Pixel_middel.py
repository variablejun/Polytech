# 영상처리를 위한 패키지를 임포트하시오.
from google.colab.patches import cv2_imshow
#######다음 완성하시오######

import numpy as np
import cv2
import matplotlib.pyplot as plt
from google.colab import drive

###########################
# 구글드라이브 마운트
drive.mount('/content/gdrive')

# 비교 이미지를 불러와 다음 변수로 각각 저장하시오.
img1 = cv2.imread('/content/gdrive/My Drive/Image_Processing/block01.png')
img2 = cv2.imread('/content/gdrive/My Drive/Image_Processing/block02.png')

#RGB 채널로 변경하기 위하여 다음을 완성하시오.

RGB_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) 
RGB_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)



#비교 이미지 저장공간 생성
output_img = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB) 

# RGB 채널 나누기
R_img1,G_img1,B_img1=cv2.split(RGB_img1)
R_img2,G_img2,B_img2=cv2.split(RGB_img2)


# 출력 array 생성하고 0으로 초기화, unsigned byte (0~255)로 설정
R_plus=np.zeros((RGB_img1.shape[0],RGB_img1.shape[1]),dtype=np.ubyte)
G_plus=np.zeros((RGB_img1.shape[0],RGB_img1.shape[1]),dtype=np.ubyte)
B_plus=np.zeros((RGB_img1.shape[0],RGB_img1.shape[1]),dtype=np.ubyte)

# 비교 알고리즘 작성
# 이미지 비교 알고리즘 및 최종 결과를 저장하는 코드를 작성하시오.



def saturation(value): #saturation함수로 정의하기
    if(value>255):
       value = 255;
    return value 
#for문을 돌며 픽셀 빼기 연산 하기
for h in range(RGB_img1.shape[0]):
  for w in range(RGB_img1.shape[1]):
    R_plus[h,w] = np.abs(np.int32(R_img1[h,w]) - np.int32(R_img2[h,w])) # 픽셀의 뺄셈이다. 결과값이 음수가 될 수 있어 abs이용해서 절대값으로 결과를 바꾼다.
    G_plus[h,w] = np.abs(np.int32(G_img1[h,w]) - np.int32(G_img2[h,w])) 
    B_plus[h,w] = np.abs(np.int32(B_img1[h,w]) - np.int32(B_img2[h,w])) 

####

#그림을 화면에 출력
plt.figure(figsize=(20,20))# 영상의 크기를 키워주자
plt.subplot(1,3,1)# 1행 3열에서 1번째 열 plt.title("First image")
plt.title("Image1")
plt.imshow(RGB_img1)
plt.axis("off")
plt.subplot(1,3,2)# 1행 3열에서 1번째 열 plt.title("First image")
plt.title("Image2")
plt.imshow(RGB_img2)
plt.axis("off")
plt.subplot(1,3,3)# 1행 3열에서 2번째 열
output_img[:,:,0]=R_plus
output_img[:,:,1]=G_plus
output_img[:,:,2]=B_plus
plt.title("Output Image")
plt.imshow(output_img)
plt.axis("off")
plt.show()