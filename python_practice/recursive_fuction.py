count =3 
def openBox():
    global count
    print("상자를 엽니다") # 3
    count -= 1
    if count == 0:
        return
    openBox()
    print("상자를 닫습니다") # 2

def addNumber(num):
    if num <= 1:
        return 1
    
    
    return num + addNumber(num - 1)

def factorial(num):
    if num <= 1:
        print('1 반환')
        return 1
    print("%d * %d! 호출" % (num, num-1))
    retVal = factorial(num - 1)
    print("%d * %d!(=%d) 반환"% (num, num-1, retVal))
    return  num * retVal

if __name__ == "__main__" :
    print(factorial(5))
# 3 번째 호출, count가 0이 되었을 때 리턴되는 것은
# 1, 2번째 호츌의 상자를 닫습니다가 나온다.
# 