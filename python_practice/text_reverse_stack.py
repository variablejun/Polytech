from ast import While
import stack_module


if __name__ == "__main__":
    with open("/Users/jeonbyeongjun/Desktop/Polytech/python_practice/outoftime.txt", 'r',encoding='UTF-8') as rfp :
        lineAry = rfp.readlines()
    # readline 한줄을 반환한다. 실행시 반환된 줄의 알파벳이 뒤집힌다    , s h t n o m   w e f   t s a l   e h T 
    # readlines 줄단 위로 반환한다. 그래서 줄단위로 뒤집힌다. 알파벳순서가 뒤집히진 않는다.
    # 전체가 뒤집어지게 어케하냐
    print("-----원본-----")
    for line in lineAry:
        stack_module.push(line)
        print(line, end=' ')
    print()    
    
    print("-----거꾸로 처리된 결과-----")
    
    fout = open("/Users/jeonbyeongjun/Desktop/Polytech/python_practice/결과.txt",'w')    
    # 쓰기모드로 파일 생성
    while True:
        line = stack_module.pop()
        if line == None :
            break
        print(line, end=' ')
        fout.write(line)
        
    fout.close()