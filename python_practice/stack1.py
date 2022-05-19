
def isStackEmpty():
    global SIZE, stack, top
    if (top <= -1): # 맨 아래층을 -1기준으로 하는데 -1보다 작거나같으면 그 스택인 비어있는 것이다.
        return True
    else:
        return False
    
def isStackFull():
    global SIZE, stack, top
    if(top >= SIZE -1):  #top 이 스택의 최대크기(사이즈 -1) 보다 크거나 같으면 스택이 꽉차있는것 
        return True
    else:
        return False

def push(data): # 스택에서 데이터를 삽입하는 것을 push라고 한다.
    global SIZE, stack, top
    if(isStackFull()): # 스택이 꽉차있는지 확인하고
        print("스택이 꽉 찼습니다.");
        return
    top += 1 # 탑을 한칸 올리고
    stack[top] = data # 그자리에 데이터 삽입

def pop(): # 스택에서 데이터를 꺼내오는 것을 pop이라고 한다.
    global SIZE, stack, top
    if (isStackEmpty()): #스택이 비어있는지 확인
        print("스택이 비었습니다.")
        return None 
    data = stack[top] # top이 가리키는 곳에 데이터를 꺼내 대입
    stack[top] = None # 그자리를 비워주고
    top -= 1 # top을 -1하여 한칸을 감소시킨다 스택은 LIFO구조기 때문에 위에서 부터 꺼내오고
    # 가장 첫번째로 들어오는 데이터가 가장 나중에 나온다.
    return data
 
def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        print("스택이 비었습니다.")
        return None
    return stack[top] #스택이 비었는지 확인후 top를 리턴하여 확인, 스택에 영향없이 확인만 한다.

SIZE = int(input("스택 크기를 입력하세요 ==> "))
stack = [None for _ in range(SIZE)] # 리스트 컴프리 핸션 
top = -1

if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
    
    while (select != 'X' and select != 'x'):
        
        if select == 'I' or select == 'i':
            data = input("입력할 데이터 ==>")
            push(data)
            print("스택 상태 : ", stack)
            
        elif select == 'E' or select == 'e':
            data = pop()
            print("추출된 데이터 ==>", data)
            print("스택 상태 : ", stack)
            
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터 ==>", data)
            print("스택 상태 : ", stack)
            
        else :
            print("입력이 잘못되었습니다.")
        
        print("TOP위치 : ",top)
        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
        
    print("프로그램 종료!")