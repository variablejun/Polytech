"""
이진트리

상위에서 하위로(조직표, 폴더구조) 계속 이어져 있는 구조, 나무가 뒤집어져 있는 구조
노드와 차수로 구성
요소들을 노드, 노드에서 나가는 것들을 차수, 차수가 0인 노드(최하위 노드) 리프노드
 

"""

def preorder(node): # 전위
    if node == None:
        return
    print(node.data, end= '->')
    preorder(node.left)
    preorder(node.right)
"""
재귀함수를 해석할 때 빠져나오는 조건을 파악하면 쉽다
순회 : 이진트리의 노드 전체를 한 번씩 방문하는 것을 순회라고 한다
전위 순회
현재 노드 데이터 처리
왼쪽 -> 오른쪽

현재 노드 데이터 출력 후
왼쪽으로 먼저 쭉 타고 내려감, 그리고 오른쪽

NONE이 나올때 까지 왼쪽부터 쭉 타고 내려가다 최하단에서 NONE을 만나면
node.left를 마무리 하고 node.right로 간다 그리고 NONE 만나면 
함수가 마무리 되고 빠져나온다

출력하고 이동
"""
def inorder(node): # 중위
    if node == None:
        return
    inorder(node.left)
    print(node.data, end= '->')
    inorder(node.right)
"""
왼쪽 으로 이동
현제 노드 출력
오른쪽으로 이동

왼쪽 최하단으로 이동후 NONE을만나면 나와서 현재 노드를 출력한다
그리고 오른쪽으로 이동하는 방식
"""
def postorder(node): # 후위
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)    
    print(node.data, end= '->')

"""
왼쪽으로 이동
오른쪽으로 이동
현재노드 처리

최상단 노드가 가장 나중에 처리된다
왼짝으로 최하단으로 이동후 NONE만나면 오른쪽으로 최하단 이동 해서
 NONE만나면 그때 나와서 현재 데이터 처리
"""
class TreeNode():
    def __init__(self):
        self.left = None # 왼쪽 차수
        self.data = None # 실제 데이터
        self.right = None # 오른쪽 차수
# L1   
node1 = TreeNode()
node1.data = '윈터'  # 최상위 노드

# L2
node2 = TreeNode()
node2.data = '카리나' # 2층 노드
node1.left = node2 # 최상위 노드의 왼쪽 차수가  node2를 가리키도록

node3 = TreeNode()
node3.data = '안유진' # 2층 노드
node1.right = node3 # 최상위 노드의 오른족 차수가 node3를 가리키도록
"""
    윈터
카리나  안유진

node1이 양쪽을 가리키게 되면서 트리구조가 완성이 된다.
"""
# L3
node4 = TreeNode()
node4.data = '장원영' # 노드2의 자식들로 node2의 왼족은 node4, 오른쪽은 node5를 가리킨다
node2.left = node4

node5 = TreeNode()
node5.data = '선미'
node2.right = node5

node6 = TreeNode() # 노드3의 자식들로 node3의 왼쪽은 node6를 가리킨다
node6.data = '아이유'
node3.left = node6
"""
            윈터
    카리나          안유진
장원영  선미    아이유
"""
# L4
node7 = TreeNode()
node7.data = '백지헌'
node4.right = node7

node8 = TreeNode()
node8.data = '이나경'
node6.right = node8
"""
                    윈터(node1)
        카리나(node2)          안유진(node3)
    장원영(node4)  선미(node5)    아이유(node6)
                    백지헌(node7)        이나경(node8)
트리구조 완성
"""
# 출력하는 방법
print(node1.data, end=' ') # node1의 데이터
print()
print(node1.left.data, node1.right.data, end=' ') # node1의 왼쪽, 오른쪽의 데이터
print()
print(node1.left.left.data, node1.left.right.data, node1.right.left.data , end=' ')
# node1의 왼쪽의 왼쪽의 데이터, 왼쪽의 오른쪽에 데이터, 오른족에 왼쪽데이터
print()
print(node1.left.left.right.data,node1.right.left.right.data , end=' ')
# node1의 왼쪽의 왼쪽의 오른쪽 데이터 ,오른족에 왼쪽의 오른쪽데이터
print()
print("---------------------------")

print('전위 순회 :', end = ' ')
preorder(node1)
print('끝')

print('중위 순회 :', end = ' ')
inorder(node1)
print('끝')

print('후위 순회 :', end = ' ')
postorder(node1)
print('끝')