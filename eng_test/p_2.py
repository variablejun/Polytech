lol = [[1,2,3],[4,5],[6,7,8,9]]
print(lol[0]) # 123 1행출력
print(lol[2][1]) # 7 3행 2열 출력
for sub in lol: # lol 행개수만큼 반복(3)
    for item in sub: # 행에 있는 요소만큼 반복 1 행은 3번, 2행은 2번, 3행은 4번
        print(item, end=' ') # 요소를 출력
    print() # 줄바꿈
#1 2 3
#4 5
#6 7 8 9