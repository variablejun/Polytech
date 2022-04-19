from tkinter import XView
import list_menu
import list_polynomial

px = [7, -4, 0 ,5] # 데이터가 계수, (배열의 길이 -1)이 지수가 된다.
# 함수를 모듈화 시켜 가져올수있다.
if __name__ == "__main__":
    pStr = list_polynomial.printPoly(px)
    print(pStr)
    
    xValue = int(input("X 값 -->"))
    
    pxValue = list_polynomial.calcPoly(xValue, px)
    print(pxValue)
# 7 * 2^3   -4 * 2^2    0 * 2^1     5 * 2^0