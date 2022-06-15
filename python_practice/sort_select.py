def findMaxldx(ary):
    maxldx = 0
    for i in range(1, len(ary)):
        if(ary[maxldx] < ary[i]):
            maxldx = i
    return maxldx

def findMinldx(ary):
    minldx = 0
    for i in range(1, len(ary)):
        if(ary[minldx] > ary[i]):
            minldx = i
    return minldx

before = [188,162,168,120,50,150,177,105]
before2 = [188,162,168,120,50,150,177,105]

aftermin = []
aftermax = []

print('정렬 전 -->', before)
for _ in range(len(before)):
    minPos = findMinldx(before)
    maxPos = findMaxldx(before2)
    
    aftermin.append(before[minPos])
    aftermax.append(before2[maxPos])
    
    print("minPos: ", minPos, "aftermin: ", aftermin)
    print("maxPos: ", maxPos, "aftermax: ", aftermax)
    del(before[minPos])
    del(before2[maxPos])
    
    print('before: ', before)
    
print('정렬(min) -->', aftermin)
print('정렬(max) -->', aftermax)