from html import entities
from pydoc import classname
from tkinter.messagebox import NO


class Node() :
    def __init__ (self):
        self.data = None
        self.link = None
        
def printNodes(start) :
    current = start
    if current == None :
        return
    
    print(current.data, end=' ')
    while current.link != None :
        current = current.link
        print(current.data, end=' ')
    print()
    

memory = []
head, current, pre = None, None, None
dataArray = ["나경","규리","지헌","지선","하영"]

if __name__ == "__main__":
    
    node = Node() # 변수에 노드 삽입
    node.data = dataArray[0] # 첫번째 데이터를 삽입한다
    head = node # 헤드라는 변수에 첫번째 데이터가 들어있는 노드를 삽입한다.
    memory.append(node) # 메모리라는 리스트 변수에 추가한다.
    
    for data in dataArray[1:] : # 0버
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)
        
    printNodes(head)
