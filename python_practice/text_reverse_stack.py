from ast import While
import stack_module


if __name__ == "__main__":
    with open("진달래꽃.txt", 'r',encoding='UTF-8') as rfp :
        lineAry = rfp.readline()
    
    print("-----원본-----")
    for line in lineAry:
        stack_module.push(line)
        print(line, end=' ')
    print()    
    
    print("-----거꾸로 처리된 결과-----")
    fout = open("결과.txt",'w')
    while True:
        line = stack_module.pop(0)
        if line == None :
            break