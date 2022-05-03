class Soojebi:
    li = ["Seoul", "Kyeonggi","Inchon", "Daejeon","Daegu","Pusan"]
    
s = Soojebi()
str01 = ''
for i in s.li: # li의 요소 만큼 i를 반복한다.
    str01 = str01 + i[0] # 각 문자열의 0번째 즉 첫번째 값만 대입하여 반복한다

print(str01) #SKIDDP