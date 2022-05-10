
def isStackEmpty():
    global SIZE, stack, top
    if (top <= -1):
        return True
    else:
        return False
    
def isStackFull():
    global SIZE, stack, top
    if(top >= SIZE -1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if(isStackFull()):
        print("스택이 꽉 찼습니다.");
        return
    top += 1
    stack[top] = data

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        print("스택이 비었습니다.")
        return None 
    data = stack[top]
    stack[top] = None
    top -= 1
    return data
 
def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        print("스택이 비었습니다.")
        return None
    return stack[top]

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