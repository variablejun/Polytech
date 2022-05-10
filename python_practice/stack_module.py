SIZE = 100
stack = [ None for _ in range(SIZE)]
top = -1
# 고정적인 수치가 필요한 경우 모듈화가 어렵다
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

def print_main() :
    print(__name__)

print("모듈 이름" + __name__ + "입니다.")
