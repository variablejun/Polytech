
def add_data(friend):
    katok.append(None) # [] 아무것도 들어있지 않은 임의의 공간을 만든다.
    kLen = len(katok) # len 함수로 리스트의 길이를 구하고 변수에 넣는다.
    katok[kLen-1] = friend # 매개변수로 들어온 값을 (리스트의 총 길이 - 1)방에 넣는다.
    # 0번재 부터 시작하기 때문에 방이 하나라서 Len이 1 이더래도 
    # 데이터를 삽입하는 공간은 리스트의 0번째 방이다.
    

def select_add_data(position,friend): # 원하는 위치를 입력해서 삽입하는 함수
    katok.append(None) 
    #빈 공간을 하나 만들고 선택한 위치에 있던 데이터를 밀어내고 그 자리에 삽입을 하는것
    kLen = len(katok) # 배열의 길이를 구한다 하나를 빼준다면 그 배열의 마지막 위치를 알 수있다.
    for i  in range(kLen-1,position,-1):  # 마지막 자리를 입력할 경우 For문은 따로 작동하지않고 바로 데이타가 추가된다.(ex 7현재위치 7입력위치)
        katok[i] = katok[i-1] # i는 배열의 현재 위치를 의미한다
        #PDF에선 2번 작업, 한칸씩 미룬다 5번째 방에 데이터를 6번째 방에 넣는작업
        # 현재위치 -1에 방에 있는 데이터를 현재 위치로 옮기는것 
        #현재 i에는 append none으로 인해 빈공간이 추가된 리스트의 -1크기를 갖고있다((리스트의 총 길이 - 1) = 현재 리스트의 위치
        katok[i-1] = None
        
    katok[position] = friend # 지정한 위치에 데이터 삽입


def del_data(position):
    katok[position] = None # 해당 위치의 데이터 삭제한다
    kLen = len(katok) 
    for i in range(position+1,kLen): # i를 지정위치+1칸부터 마지막칸까지
        katok[i -1] = katok[i] # 현재 위치의 데이터를 한칸 전으로 옮기고
        katok[i] = None # 다시 현재 위치를 비운다

    del(katok[kLen-1]) # 비어있는 마지막 칸을 지운다



katok = []
select_menu = 0

def print_main() :
    print(__name__)

print("모듈 이름" + __name__ + "입니다.")

if __name__ == "__main__" : # 다른 모듈에서 호출 시 아래 코드는 실행하지 않고 함수만 가져온다.
    while(select_menu!=4):
        select_menu = int(input("선택하세요 1: 추가, 2: 삽입, 3: 삭제, 4: 종료 -->"))
        # input 함수는 scanf와 같은 기능을 하나 텍스트로 반환되기때문에 캐스팅을 거치거나 
        # 조건의 숫자를 텍스트로 받아야한다.
        
        if(select_menu == 1):
            data = input("추가할 데이터-->")
            if (data==""):
                print("데이터를 입력 하세요.")
                continue
            add_data(data)
            print(katok)
            
        elif(select_menu == 2):
            posi = int(input("삽입할 위치-->"))
            if posi >= len(katok):
                print("배열 범위 밖입니다.")
                continue
            data = input("추가할 데이터-->")
            if (data==""):
                print("데이터를 입력 하세요.")
                continue
            
            select_add_data(posi, data)
            print(katok)     
        
        elif(select_menu == 3):
            posi = int(input("삭제할 위치-->"))
            if posi >= len(katok):
                print("배열 범위 밖입니다.")
                continue
            del_data(posi)
            print(katok) 
        
        elif(select_menu == 4):
            print(katok)
            exit
            
        else :
            print("1 ~ 4 중 하나를 입력하세요.")
            continue       