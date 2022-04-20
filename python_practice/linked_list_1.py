from hashlib import new
from os import link


class Node(): # Node 라는 구조체(데이터형)를 만든것, 실행하면 자동으로 실행되어 데이터와 링크부분이 생성된다
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = "나경" 

node2 = Node()
node2.data = "하영" 
node1.link = node2

node3 = Node()
node3.data = "지헌" 
node2.link = node3

node4 = Node()
node4.data = "지선" 
node3.link = node4

node5 = Node()
node5.data = "규리" 
node4.link = node5

newNode = Node()
newNode.data = "병준"
newNode.link = node2.link # node2의 링크값인 node3을 새로 삽입할 노드 링크에 넣는다
node2.link = newNode # 그리고 node2가 newNode를 가리키도록 삽입한다.

node2.link = newNode.link # newnode 가 가리키는 node3를 node2 링크에 넣어주고 뉴노드 삭제
del(newNode)
# print(node1.data, end=' ')
# print(node1.link.data, end=' ')
# print(node1.link.link.data, end=' ')
# print(node1.link.link.link.data, end=' ')
# print(node1.link.link.link.link.data, end=' ')

current = node1 # 변수에 헤드를 넣고 
print(current.data, end=' ') # 헤드 출력
while current.link != None : # 링크가 None이 아닐때 까지
    current = current.link # 현제 헤드인 node1에 링크엔 node2가 들어가있다 
    # 현재 link 안에 node2를 입력해주는것
    
    print(current.data, end=' ') # 입력받은 링크값(node2)의 데이터를 출력
    