def isQueueFull(): # 꽉찻는지 확인
    global SIZE, queue, front, rear
    if((rear + 1) % SIZE == front): # 리어 +1 과 큐의 지정한 크기인 SIZE와 나누었을 때 
        # 나머지가 프론트와 같으면 큐에 빈자리가 없는 것이다.
        # 리어와 프론트는 한칸 차이가 나도록 설계되어있다 
        # 이때 1을 더해서 사이즈로 %연산을 하면 사이즈보다 작아 자기자신이 나머지로 나오게 되는데
        # 그것과 프론트가 같으면 빈자리가 없다는 것이다, 한칸의 여유를 두어야 하기 때문이다.
        
        return True
    else:
        return False
    
    
def isQueueEmpty(): #비어있는 지 확인
    global SIZE, queue, front, rear
    if (front == rear): # 둘이 같은 위치에 있다면 큐가 비엇다는 것이다
        # 한칸차이가 나게 설계하지 않으면 큐가 비었는지 꽉찻는지 구분할 수가 없다.
        # 그래서 비었을땐 이렇게 비교하지만 꽉찻을 경우엔 (rear + 1) % SIZE == front로 비교한다.
        return True
    else :
        return False
    
def enQueue(data): # 데이터삽입
    global SIZE, queue, front, rear
    if(isQueueFull()): # 꽉찻는지 확인해서 TRUE반환시 함수 종료
        print("큐가 꽉 찼습니다.")
        return   
    rear = (rear + 1)  % SIZE # 꽉차지 않았으면 마지막 위치를 가리키게 하고 데이터 삽입
    # (rear + 1)  % SIZE 가 원형큐의 마지막위치를 가리킨다고 생각하면 된다.
    # (rear + 1)  % SIZE를 풀에서 이용했던 것도 Front와 마지막위치가 같으면 원형큐가 꽉 찬것이기 때문이다.
    queue[rear] = data # 데이터 삽입

def deQueue(): #데이터 추출하는 함수
    global SIZE, queue, front, rear
    if(isQueueEmpty()): #비어있는지 확인하고 TRUE반환시 함수 종료 
        print("큐가 비었습니다.")
        return None  
    front = (front + 1) % SIZE # 프론트는 0부터 시작한다 첫번째 자리는 NONE이기 때문에 1을더해준 것(0)과 사이즈를 %연산하면 첫번째 자리가 나온다
    # 큐는 FIFO구조기 때문에 먼저 들어온것이 먼저나간다
    data = queue[front] # 데이터를 추출하고
    queue[front] = None #비워준다
    return data

def peek():
    global SIZE, queue, front, rear
    if(isQueueEmpty()):
        print("큐가 비었습니다.")
        return None 
    return queue[(front + 1) % SIZE] #첫번째 자리에 데이터가 무었이 있는지 확인하는 함수

SIZE = int(input("큐의 크기를 입력하세요 -->"))
queue = [None for _ in range(SIZE)]
front = rear = 0

##메인 코드 부분 ##
if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택==>")

    while (select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input("입력한 데이터==>")
            enQueue(data)
            print("큐 상태:",queue)
            print("front : ", front, ", rear : ", rear)
            
        elif select == 'E' or select == 'e':
            data = deQueue()
            print("추출된 데이터==>",data)
            print("큐 상태 : ",queue)
            print("front : ", front, ", rear : ", rear)  
                     
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터==>",data)
            print("큐 상태:",queue)
            print("front : ", front, ", rear : ", rear)
                       
        else:
            print("입력이 잘못 됨")

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택==>")

print("프로그램 종료!")