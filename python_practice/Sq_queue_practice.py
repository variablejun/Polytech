def isQueueFull():
    global SIZE, queue, front, rear
    if(rear != SIZE-1):# 리어와 큐의 마지막 자리가 같지 않으면 FALSE
        return False
    elif (rear == SIZE -1) and (front == -1):
        return True
     # 데이터의 마지막과 큐전체크기-1(마지막 방)이 같을 경우 
        # 그리고 프론트(데이터의 처번째 자리)가 -1과 같다면 큐에는 빈자리가 없다는 것
        
    else :# 입력된 데이터를 추출한 뒤에 처리하는 방법이다
        # rear != SIZE-1 문은 맞기 때문에 elif로 넘어가는데
        # (rear == SIZE -1) and (front == -1) 중 앞에 조건은 참이지만 뒤에 조건은 참이 아니다
        # 큐 구조상 추출시 앞에서 부터 나오기 때문에 리어위치는 그대로이고 끝까지 차있다고 나오지만
        # 막상 프론트는 추출되었기 때문에 -1위치에 있지 않다 
        # 그래서 추출한 뒤는 else문을 통해 한칸씩 앞당겨서 뒤에 데이터가 추가될 자리를 마련해주고 
        # 큐 구조가 유지될 수 있도록 한다
        
        for i in range(front +1, SIZE): # 0부터 시작하기 위해 1 더해줌, 0부터 큐의 지정한 크기만큼 반복
            queue[i - 1] = queue[i] # 현재 자리의 데이터를 -1자리에 대입해준다
            queue[i] = None # 그리고 현재 자리를 비워준다
        front -=1
        # 프론트와 니어를 하나씩 감소시켜준다
        rear -= 1
        # 데이터 입력 전에 한칸씩 당겨주면서 리어와 프론트 위치도 바뀌어야 하기 때문이다.
        return False # FALSE를 반환하여 if문이 수행되지 않도록 한다.
    
def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear): # 프론트와 리어가 같다면 큐에는 아무것도 없는 것이므로 
        #비었다고 확인할 수 있다.
        return True
    else :
        return False
    
def enQueue(data):
    global SIZE, queue, front, rear
    if(isQueueFull()):
        print("큐가 꽉 찼습니다.")
        return   # 큐에 빈자리가 있는지 확인
    rear += 1 # 리어를 하나 증가시켜주고 
    queue[rear] = data # 그 리어 자리에 데이터 삽입

def deQueue():
    global SIZE, queue, front, rear
    if(isQueueEmpty()):
        print("큐가 비었습니다.")
        return None  # 큐가 비었는지 확인
    front +=1 # 프론트를 하나 더한다 -1위치에 있던 프론트가 0으로 변함
    data = queue[front] # 그 0번째 자리에 데이터를 꺼내서 대입
    queue[front] = None # 빈자리로 만들어준다
    return data # 꺼낸 데이터를 반환한다.

def peek():
    global SIZE, queue, front, rear
    if(isQueueEmpty()): 
        print("큐가 비었습니다.")
        return None  # 비었는지 확인
    return queue[front + 1] # 0자리를 가리키기 위해 더해주고 반환해준다 
    # 기존 큐에 영향없이 확인만 한다

SIZE = int(input("큐의 크기를 입력하세요 -->"))
queue = [None for _ in range(SIZE)] # i변수 안쓸 때 _, 입력한 SIZE만큼 반복하여 NONE이 들어간 배열생성
front = rear = - 1 # 시작위치는 둘다 -1 

##메인 코드 부분 ##
if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택==>")

    while (select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input("입력한 데이터==>")
            enQueue(data)
            print("큐 상태:",queue)
            
        elif select == 'E' or select == 'e':
            data = deQueue()
            print("추출된 데이터==>",data)
            print("큐 상태==>",queue)
            
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터==>",data)
            print("큐 상태:",queue)
            
        else:
            print("입력이 잘못 됨")

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택==>")

print("프로그램 종료!")