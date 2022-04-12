from tkinter import XView
import list_menu
import list_polynomial

px = [7, -4, 0 ,5]
# 함수를 모듈화 시켜 가져올수있다.
if __name__ == "__main__":
    pStr = list_polynomial.printPoly(px)
    print(pStr)
    
    xValue = int(input("X 값 -->"))
    
    pxValue = list_polynomial.calcPoly(xValue, px)
    print(pxValue)