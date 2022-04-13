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

def  calcPoly(xVal, p_x): # 실제로 게산해 주는 함수
    retValue = 0
    term = len(p_x) -1 # 지수는 0부터 시작한다 하지만 
    #len함수로 길이를 구할 경우 0~3을 4로 반환하기 때문에 1개를 빼준다
    
    for i in range(len(p_x)):
        coef = p_x[i]
        retValue = retValue + coef * xVal ** term
        # 식을 출력해야 할땐 str 변수로 캐스팅 해주지만 이 함수는
        #계산을 해야해서 캐스팅을 하지 않는다 **제곱수 연산

        term = term - 1 #지수 감소
    
    return retValue


def print_main() :
    print(__name__)

print("모듈 이름" + __name__ + "입니다.")
