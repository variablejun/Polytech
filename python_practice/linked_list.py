
class Node():
    def __init__(self):
        self.data = None
        self.link = None
        
def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
        
    print()

def insertNode(findData, insertData):
    global memory, head, current, pre
    
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    current = head
    
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
        
    node = Node()
    node.data = insertData
    current.link = node
    
memory = []
head, current, pre = None, None, None
dataArray = ["나경","규리","하영","지선","지헌"]
if __name__ == "__main__" :
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)
    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)
    printNodes(head)
    insertNode("나경","유빈")
    printNodes(head)
    insertNode("지선","승희")
    printNodes(head)
    insertNode("재남","아린")        
    printNodes(head)       