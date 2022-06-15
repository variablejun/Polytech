from traceback import print_tb


def findInsertldx(ary, data):
    findldx = -1
    for i in range(0, len(ary)):
        if(ary[i] > data):
            findldx = i
            break
    
    if findldx == -1 :
        return len(ary)
    else :
        return findldx
    
before = [188,162,168,120,50,150,177,105]
after = []

print("정렬 전 -->", before)
for i in range(len(before)):
    data = before[i]
    insPos = findInsertldx(after, data)
    after.insert(insPos,data)
    print("data:", data," insPos:", insPos," after:",after)
print("정렬 후 -->", after)