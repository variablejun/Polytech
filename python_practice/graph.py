

class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
        
G1 = Graph(4)
G1.graph[0][1]= 1; G1.graph[0][2]= 1;G1.graph[0][3]= 1 # A
G1.graph[1][0]= 1; G1.graph[1][2]= 1 # B
G1.graph[2][0]= 1; G1.graph[2][1]= 1; G1.graph[2][3]= 1 # C
G1.graph[3][0]= 1; G1.graph[3][2]= 1; # D

print('## G1 무방향 그래프 ##')
for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end = ' ')
    print()
    
G3 = Graph(4)
G3.graph[0][1] = 1; G3.graph[0][2] = 1
G3.graph[3][0] = 1; G3.graph[3][2] = 1

print('## G3 방향 그래프 ##')
for row in range(4):
    for col in range(4):
        print(G3.graph[row][col], end = ' ')
    print()
    
    
G4 = Graph(4)
G4.graph[0][3] = 1;
G4.graph[1][2] = 1; G4.graph[1][3] = 1
G4.graph[2][1] = 1; 
G4.graph[3][0] = 1; G4.graph[3][1] = 1
print('## G4 방향 그래프 ##')
for row in range(4):
    for col in range(4):
        print(G4.graph[row][col], end = ' ')
    print()
    
G5 = None
stack = []
visitiedAry = [] # 방문한 정점

G5 = Graph(4)
G5.graph[0][2] = 1; G5.graph[0][3] =1
G5.graph[1][2] = 1; 
G5.graph[2][0] = 1; G5.graph[2][1] =1;G5.graph[2][3] = 1
G5.graph[3][0] = 1; G5.graph[3][2] =1

print('## G5 무방향 그래프 ##')
for row in range(4):
    for col in range(4):
        print(G5.graph[row][col], end = ' ')
    print()
    
current = 0 # 시작 정점 A
stack.append(current)
visitiedAry.append(current)

while (len(stack) != 0):
    next = None
    for vertex in range(4):
        if G5.graph[current][vertex] == 1:
            if vertex in visitiedAry: # 방문한 적이 있는 정점이면 탈락
                pass
            else:# 방문한 적이 없으면 다음 정점으로 지정
                next = vertex
                break
    print("cur : ", current, "ver : ", vertex, "next : ", next)
    if next != None : # 다음에 방문할 정점이 있는경우
        current = next
        stack.append(current)
        visitiedAry.append(current)
        print("current : ", chr(ord('A') + current), "stack:", stack)
    else: # 다음에 방문할 정점이 없는경우 
        current = stack.pop()
        print("pop : ", chr(ord('A') + current), "stack:", stack)
    
print('방문 순서 -->', end= ' ')
for i in visitiedAry:
    print(chr(ord('A') + i), end= ' ')


