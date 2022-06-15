from re import I


def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minldx = i
        for k in range(i+1,n):
            print("k :", k)
            if(ary[minldx] > ary[k]):
                minldx = k
        tmp = ary[i]
        ary[i] = ary[minldx]
        ary[minldx] = tmp
        print("minldx: ", minldx, "i: ",i)
    
    return ary
dataAry = [188,162,168,120,50,150,177,105] 

print("정렬 전 -->", dataAry)     
dataAry = selectionSort(dataAry)
print("정렬 후 -->", dataAry)         