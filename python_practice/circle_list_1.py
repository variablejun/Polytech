
class Node():
    def __init__(self):
        self.data = None
        self.link = None
        
def printNodes(start): #노드 출력
    current = start
    if current == None: # 노드가 비어있다면 함수를끝낸다.
        return
    print(current.data, end=' ') # 헤드를 먼저 출력한다
    while current.link != start: # 헤드가 아닐때까지
        current = current.link # 해당 링크를 (node2) 커런트에 넣고 출력
        print(current.data, end=' ')
        
    print()

def insertNode(findData, insertData): # 입력된 데이터를 찾아 그 앞에 데이터를 삽입하고 
    #끝까지 찾아서 없으면 맨뒤에 삽입
    global memory, head, current, pre #글로벌 전역변수선언
    
    if head.data == findData: # 헤드 노드첫번째 데이터와 같을 경우 처리
        node = Node()  
        node.data = insertData  
        node.link = head   
        last = head# 마지막 노드를 첫 번째 노드로 우선 지정
        while last.link != head : # 마지막 노드를 찾으면 반복종료
            last = last.link # 라스트를 다음 노드로 변경
        last.link = node # 마지막 노드 링크에 새 노드 지정
        
        head = node 
        return
    
    current = head
    
    while current.link != head: # 현재노드의 링크가 헤드가 아닐경우 즉 마지막자리가 아닐경우 반복 
        pre = current 
        current = current.link  
        if current.data == findData: 
            node = Node()  
            node.data = insertData 
            node.link = current 
            pre.link = node  
            return
        
    node = Node() # 찾지 못했을 경우 노드를 생성하고
    node.data = insertData # 삽입된 데이터를 넣어주고
    current.link = node # 현재 노드 링크에 새로 삽입될 노드를 넣어준다
    node.link = head

def deleteNode(deleteData):
    global memory, head, current, pre
    if head.data == deleteData: # 첫번째 노드 삭제
        current = head
        head = head.link
        last = head
        while last.link != current: # 마지막 노드를 찾으면 반복종료
            last = last.link # last 를 다음 노드로 변경하면서 마지막 노드 찾을 때 까지 반복
        last.link = head # 마지막 노드의 링크에 헤드가 들어가면서 원형 리스트 구현
        del(current)
        return
    
    current = head
    while current.link != head: # 두번째 노드 삭제
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return
'''        
def findNode(findData):
    global memory, head, current, pre    
    current = head
    if current.data == findData :
        return current
    while current.link != head :
        current = current.link
        if current.data == findData:
            return current
    return Node()
'''

def findNode(findData) : 
    global memory, head, current, pre 
    current = head 
    if current.data == findData : 
        return current 
    while current.link != head : 
       current = current.link 
       if current.data == findData : 
           return current 
    return Node()

"""
current.link != None 
나경 규리 하영 지선 지헌 
유빈 나경 규리 하영 지선 지헌 
유빈 나경 규리 하영 승희 지선 지헌
유빈 나경 규리 하영 승희 지선 지헌 아린
나경
아린
지선
유빈 나경 규리 하영 승희 지선 지헌
유빈 나경 규리 하영 지선 지헌
유빈 규리 하영 지선 지헌
규리 하영 지선 지헌

head.link != None
나경 규리 하영 지선 지헌 
유빈 나경 규리 하영 지선 지헌 
유빈 나경 규리 하영 승희 지선 지헌
유빈 나경 규리 하영 승희 지선 지헌 아린
나경
아린
지선
유빈 나경 규리 하영 승희 지선 지헌
유빈 나경 규리 하영 지선 지헌
유빈 규리 하영 지선 지헌
규리 하영 지선 지헌
"""
memory = []
head, current, pre = None, None, None
dataArray = ["나경","규리","하영","지선","지헌"]

if __name__ == "__main__" :
    #헤드 처리
    node = Node() # 노드 생겅
    node.data = dataArray[0] # 0번째 방의 데이터 삽입
    head = node # 헤드에 노드 삽입
    node.link = head
    memory.append(node) # 메모리 리스트 에 추가
    
    for data in dataArray[1:]: # 데이터어레이 1번째부터 끝까지 반복
        pre = node # 현재 가리키고 있는 노드를 pre에 삽입 첫번째라면 헤더
        node = Node() #노드 생성
        node.data = data # for문에서 가리키는 데이터 삽입
        pre.link = node # 바로 전(첫번째 라면 헤더)에 노드의 링크에 노드를 삽입하여 가리키게함
        node.link = head
        memory.append(node) # 메모리 리스트에 추가
        
    printNodes(head) #헤드만 넣어도 전부출력
    insertNode("나경","유빈")
    printNodes(head)
    insertNode("지선","승희")
    printNodes(head)
    insertNode("재남","아린")
    printNodes(head)
    
    fNode = findNode("나경")   
    print(fNode.data) 
    fNode = findNode("아린")   
    print(fNode.data) 
    fNode = findNode("지선")   
    print(fNode.data) 
                
  
    deleteNode("아린")        
    printNodes(head)  
    deleteNode("승희")        
    printNodes(head)  
    deleteNode("나경")        
    printNodes(head)
    deleteNode("유빈")        
    printNodes(head)       