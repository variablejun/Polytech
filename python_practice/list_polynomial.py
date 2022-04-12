def printPoly(p_x) : # 계산식을 출력해 주는 함수
    term = len(p_x) -1
    polyStr = "P(x) = "
    
    for i in range(len(p_x)): # 리스트의 길이만큼 반복
        coef = p_x[i]  # 리스트 안에 데이터를 집어넣어준다,
        
        if (coef >= 0):
            polyStr = polyStr + "+" # 데이터 앞에 + 기호 넣어주어 양수임을 확인..?
        polyStr = polyStr + str(coef) + "x^" + str(term) + " "# 기호 계수 x^ + 지수
        term = term - 1 # 출력이 끝난 지수를 하나 감소시킨다 지수는 감소하고 계수가 들어있는 리스트 위치는 증가한다.
    
    return polyStr # 문자열반환

def  calcPoly(xVal, p_x):
    retValue = 0
    term = len(p_x) -1
    
    for i in range(len(p_x)):
        coef = p_x[i]
        retValue = retValue + coef * xVal ** term
        term = term - 1
    
    return retValue


def print_main() :
    print(__name__)

print("모듈 이름" + __name__ + "입니다.")
