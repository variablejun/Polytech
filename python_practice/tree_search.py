
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None
        
memory = [] # 메모리 준비
root = None # root 초기화

# 배열에 있는 데이터 이진트리 삽입
nameAry = ['아이브','르세라핌','프로미스나인','오마이걸','에스파','블랙핑크']

# 첫번째 데이터 삽입
node = TreeNode()
node.data = nameAry[0] # 0 번째방에 데이터를 첫번째 노드에 넣는다

root = node # root가 첫번째 노드를 가리키도록 대입시켜준다.
memory.append(node) # 리스트에 첫번째 노드 삽입
"""
이진 탐색 트리

데이터 크기를 기준으로 일정한 형태를 구성된 트리
문자열의 경우 가나다라 순으로 크기가 나뉘어 정렬됨

루트 기준으로 왼쪽 서브트리는 루트 노드보다 작은 값을가지고
오른쪽트리는 루트보다 큰 값을 가진다.
각 서브 트리도 같은 특징을 가진다.

"""
for name in nameAry[1:]: # 0번째 방을 제외한 배열 반복
    node = TreeNode() # 새 노드 생성
    node.data = name # 두번째 방에 데이터 입력
    current = root  # 현재 작업노드를 루트 노드로 지정
    
    while True:
        if name < current.data : # 현재 노드의 데이터와 배열의 데이터
            # 비교하여 현재 노드 데이터가 더 크면
            if current.left == None: #왼쪽 노드가 비어있다면
                current.left = node # 새 노드를 왼쪽에 연결
                break
            current = current.left # 그리고 left를 
            # 현재 노드에 넣어주고 다음 번째 데이터 삽입시 비교
            # 그렇게 반복하여 작으면 왼쪽 크면 오른쪽으로 정렬시킨다 
        else :
            if current.right == None:
                current.right = node
                break
            current = current.right
    memory.append(node) #

print("이진 탐색 트리 구성 완료!")

findName = input("찾고자 하는 걸그룹을 입력하세요 : ")
current = root
while True :
    if findName == current.data : 
        print(findName, '을(를) 찾음.')
        break
    elif findName < current.data : 
        # 찾으려는 노드의 데이터와 현재 노드의 데이터를 비교해서
        # 작으면 왼쪽 크면 오른쪽을 탐색하게 만들어준다.,
        # 만약에 NONE이 나올때 까지 못찾으면 트리에 없는것
        if current.left == None:
            print(findName, '이(가) 트리에 없음')
            break
        current = current.left # 현재노드 갱신
    else :
        if current.right == None:
            print(findName, '이(가) 트리에 없음')
            break
        current = current.right # 현재노드 갱신   

# 이진트리 삭제

deleteName = '소녀시대'

current = root
parent = None
while True:
    
    if deleteName == current.data: 
        #아래 조건문은 일단 현재 데이터와 삭제데이터가
        # 같을경우 작동한다.
        if current.left == None and current.right == None:
            # 왼쪽과 오른쪽 모두 NONE 이라면 
            # 이것응 리프 노드 이다
            
            # 그래서 부모 노드의 왼쪽이 현재노드와 같다면
            if parent.left == current: 
                # 해당 노드를 NONE으로 바꾸어준다.
                parent.left = None
            else:
                # 오른쪽일 경우에도 NONE으로 바꿔준다
                parent.right = None
                
            del(current) # 현재 삭제
        
        elif current.left != None and current.right == None:
            # 왼쪽이 NONE이 아니고 오른쪽만 NONE /왼쪽노드에 자식이 있다
            # 즉 리프노드가 아닌 자식노드가 있는경우
            # 완쪽에 자식노드가 있는 경우
            if parent.left == current: 
                # 현재 노드와 부모의 left노드가 같다면
                parent.left = current.left
                # 부모의 왼족노드에 현재노드의 왼쪽 자식노드 삽입
            else: # 오른쪽과 같다면
                parent.right = current.left
                # 부모의 오른쪽 노드에 왼쪽 자식노드 삽입 후 삭제
            del(current) # 현재노드 삭제
            
        elif current.left == None and current.right != None:
            # 오룬쪽이 NONE이 아니고 왼쪽만 NONE
            # 현재 노드의 오른쪽 링크에 자식이 있다.
            
            if parent.left == current:
                # 부모의 오른쪽에 현재 노드가 있는지 왼쪽에 있는지 확인
                
                parent.left = current.right
            # 마찬가지로 비교해서 부모의 왼쪽노드에 
            # 현재노드의 오른쪽 링크 노드 삽입 
            else:
                parent.right = current.right
                
            del(current)
        print(deleteName, '이(가) 삭제됨.')
        break 
    #
    elif deleteName < current.data: # 삭제할 데이터가 작을때(왼족)
        if current.left == None:
            print(deleteName, '이(가) 트리에 없음')  
            break
        parent = current # 현재 노드가 부모 노드가 되고
        current = current.left # 왼쪽링크노드가 현재 노드가 된다
        
    else :# 삭제할 데이터가 클때(왼족)
        if current.right == None:
            print(deleteName, '이(가) 트리에 없음')
            break
        
        parent = current# 현재 노드가 부모 노드가 되고
        current = current.right# 오른쪽링크노드가 현재 노드가 된다
   
