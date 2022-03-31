from operator import add


katok = []
def add_data(friend):
    katok.append(None) # [] 아무것도 들어있지 않은 임의의 공간을 만든다.
    kLen = len(katok) # len 함수로 리스트의 길이를 구하고 변수에 넣는다.
    katok[kLen-1] = friend # 매개변수로 들어온 값을 (리스트의 총 길이 - 1)방에 넣는다.
    # 0번재 부터 시작하기 때문에 방이 하나라서 Len이 1 이더래도 
    # 데이터를 삽입하는 공간은 리스트의 0번째 방이다.
    
add_data('지헌')
add_data('나경')
add_data('하영')
add_data('지선')
add_data('규리')

print(katok)

def select_add_data(position,friend): # 원하는 위치를 입력해서 삽입하는 함수
    katok.append(None) 
    #빈 공간으 하나 만들고 선택한 위치에 있던 데이터를 밀어내고 그 자리에 삽입을 하는것
    kLen = len(katok) # 배열의 길이를 구한다 하나를 빼준다면 그 배열의 마지막 위치를 알 수있다.
    for i  in range(kLen-1,position,-1):  # 마지막 자리를 입력할 경우 For문은 따로 작동하지않고 바로 데이타가 추가된다.(ex 7현재위치 7입력위치)
        katok[i] = katok[i-1] # i는 배열의 현재 위치를 의미한다
        #PDF에선 2번 작업, 한칸씩 미룬다 5번째 방에 데이터를 6번째 방에 넣는작업
        # 현재위치 -1에 방에 있는 데이터를 현재 위치로 옮기는것 
        #현재 i에는 append none으로 인해 빈공간이 추가된 리스트의 -1크기를 갖고있다((리스트의 총 길이 - 1) = 현재 리스트의 위치
        katok[i-1] = None
        
    katok[position] = friend # 지정한 위치에 데이터 삽입
    
select_add_data(2,'새롬')
print(katok)
select_add_data(6,'서연')
print(katok)


def del_data(position):
    katok[position] = None # 해당 위치를 삭제한다
    kLen = len(katok) 
    for i in range(position+1,kLen): # i를 지정위치+1칸부터 마지막칸까지
        katok[i -1] = katok[i] # 현재 위치의 데이터를 한칸 전으로 옮기고
        katok[i] = None # 다시 현재 위치를 비운다

    del(katok[kLen-1]) # 비어있는 마지막 칸을 지운다

del_data(2)
print(katok)
del_data(3)
print(katok)
