
class Node():
    def __init__(self):
        self.data = None
        self.link = None
        
def printNodes(start): #노드 출력
    current = start
    if current == None: # 노드가 비어있다면 함수를끝낸다.
        return
    print(current.data, end=' ') # 헤드를 먼저 출력한다
    while current.link != None: # 그다음 링크를 통해 링크가 None일때 까지 반복
        current = current.link # 해당 링크를 (node2) 커런트에 넣고 출력
        print(current.data, end=' ')
        
    print()

def insertNode(findData, insertData): # 입력된 데이터를 찾아 그 앞에 데이터를 삽입하고 
    #끝까지 찾아서 없으면 맨뒤에 삽입
    global memory, head, current, pre #글로벌 전역변수선언
    
    if head.data == findData: # 헤드 노드첫번째 데이터와 같을 경우 처리
        node = Node() # 헤드 앞에 넣을 노드 생성
        node.data = insertData # 데이터 부분에 입력된 데이터를 입력한다.
        node.link = head # 링크를 헤드를 가리키도록 한다 -> 현재 헤드는 입력받기 전 노드이다 
        #이제 두번째가 되어 헤더가 아니라서 헤드를 링크에 넣어서 두번째가 될 자신을 가리키게 한다.
        head = node # 이제 헤드에 노드를 넣어서 완성한다
        return
    
    current = head
    
    while current.link != None: # 링크가 None이 아니고 찾는 데이터가 헤드가 아닐때
        pre = current # 현재 노드를 pre에 넣고
        current = current.link # 링크를 현재 노드에 넣음으로 써 한칸씩 링크를 타고 나아간다
        if current.data == findData:# 그러다 찾는 데이터와 현제 데이터가 같으면
            node = Node() # 새로운 노드를 생성하고
            node.data = insertData # 입력된 데이터를 삽입한다.
            node.link = current# 링크는 현재 노드를 가리키게 하고(종국엔 다음 노드가 된다.)
            pre.link = node # 바로전 노드인 pre는 현재 새로 추가된 노드를 갖게된다.
            return
        
    node = Node() # 찾지 못했을 경우 노드를 생성하고
    node.data = insertData # 삽입된 데이터를 넣어주고
    current.link = node # 현재 노드 링크에 새로 삽입될 노드를 넣어준다

def deleteNode(deleteData):
    global memory, head, current, pre
    if head.data == deleteData: # 첫번째 노드 삭제
        current = head
        head = head.link
        del(current)
        return
    
    current = head
    while current.link != None: # 두번째 노드 삭제
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return
        
memory = []
head, current, pre = None, None, None
dataArray = ["나경","규리","하영","지선","지헌"]

if __name__ == "__main__" :
    #헤드 처리
    node = Node() # 노드 생겅
    node.data = dataArray[0] # 0번째 방의 데이터 삽입
    head = node # 헤드에 노드 삽입
    memory.append(node) # 메모리 리스트 에 추가
    
    for data in dataArray[1:]: # 데이터어레이 1번째부터 끝까지 반복
        pre = node # 현재 가리키고 있는 노드를 pre에 삽입 첫번째라면 헤더
        node = Node() #노드 생성
        node.data = data # for문에서 가리키는 데이터 삽입
        pre.link = node # 바로 전(첫번째 라면 헤더)에 노드의 링크에 노드를 삽입하여 가리키게함
        memory.append(node) # 메모리 리스트에 추가
        
    printNodes(head) #헤드만 넣어도 전부출력
    insertNode("나경","유빈")
    printNodes(head)
    insertNode("지선","승희")
    printNodes(head)
    insertNode("재남","아린")        
    printNodes(head)  
    deleteNode("아린")        
    printNodes(head)     