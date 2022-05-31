def preorder(node): # 전위
    if node == None:
        return
    print(node.data, end= '->')
    preorder(node.left)
    preorder(node.right)

def inorder(node): # 중위
    if node == None:
        return
    inorder(node.left)
    print(node.data, end= '->')
    inorder(node.right)
    
def postorder(node): # 후위
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)    
    print(node.data, end= '->')


class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None
# L1   
node1 = TreeNode()
node1.data = '윈터'

# L2
node2 = TreeNode()
node2.data = '카리나'
node1.left = node2

node3 = TreeNode()
node3.data = '안유진'
node1.right = node3

# L3
node4 = TreeNode()
node4.data = '장원영'
node2.left = node4

node5 = TreeNode()
node5.data = '선미'
node2.right = node5

node6 = TreeNode()
node6.data = '아이유'
node3.left = node6

# L4
node7 = TreeNode()
node7.data = '백지헌'
node4.right = node7

node8 = TreeNode()
node8.data = '이나경'
node6.right = node8

print(node1.data, end=' ')
print()
print(node1.left.data, node1.right.data, end=' ')
print()
print(node1.left.left.data, node1.left.right.data, node1.right.left.data , end=' ')
print()
print(node1.left.left.right.data,node1.right.left.right.data , end=' ')
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