class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g):
    print(' ', end= ' ')
    for v in range(g.SIZE):
        print(nameAry[v], end= ' ')
    print()
    for row in range(g.SIZE):
        print(nameAry[row], end=' ')
        for col in range(g.SIZE) :
            print(g.graph[row][col], end = ' ')
        print()
        
    print()

def findVertex(g, findVtx):
    while (len(stack) != 0):
        next = None
    for vertex in range(4):
        if G1.graph[current][vertex] == 1:
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
       
     
G1 = None
nameAry = ['춘천','서울','속초','대전','광주','부산']
춘천,서울,속초,대전,광주,부산 = 0,1,2,3,4,5

gSize = 6
G1 = Graph(gSize)
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15
G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40;G1.graph[서울][대전] = 11; G1.graph[서울][광주] = 50

G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40;G1.graph[속초][대전] = 12
G1.graph[대전][춘천] = 11; G1.graph[대전][속초] = 12;G1.graph[대전][광주] = 20; G1.graph[대전][부산] = 30


G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20;G1.graph[광주][부산] = 25
G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25

print('## 자전거 도로 건설을 위한 전체 연결도 ##')
printGraph(G1)

edgeAry = []
for i in range(gSize):
    for k in range(gSize):
        if G1.graph[i][k] != 0:
            edgeAry.append([G1.graph[i][k]], i, k)
            
from operator import itemgetter
edgeAry = sorted(edgeAry, key=itemgetter(0),reverse=True)
