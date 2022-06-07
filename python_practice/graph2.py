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

G1 = None
nameAry = ['카즈하','장원영','안유진','카리나','헤이즈','아이유']
카즈하, 장원영, 안유진, 카리나, 헤이즈, 아이유 = 0,1,2,3,4,5
gSize = 6

G1 = Graph(gSize)
G1.graph[카즈하][장원영]= 1; G1.graph[카즈하][안유진]= 1
G1.graph[장원영][카즈하]= 1; G1.graph[장원영][카리나]= 1
G1.graph[안유진][카즈하]= 1; G1.graph[안유진][카리나]= 1
G1.graph[카리나][장원영]= 1; G1.graph[카리나][안유진]= 1;G1.graph[카리나][헤이즈]= 1; G1.graph[카리나][아이유]= 1
G1.graph[헤이즈][카리나]= 1; G1.graph[헤이즈][아이유]= 1
G1.graph[아이유][카리나]= 1; G1.graph[아이유][헤이즈]= 1
print('## G1 무방향 그래프 ##')
printGraph(G1)


