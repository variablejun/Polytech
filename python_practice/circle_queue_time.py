
import circle_queue_module
circle_queue_module.SIZE = 10
# 미완
if __name__ == "__main__":
    waiting = [('고장/수리',3),
               ('사용문의',9),
               ('환불문의',4),
               ('기타문의',1)
               ]
    
    select = input("예약(I)/완료E)/대기시간확인(V)/종료(X) 중 하나를 선택==>")
    sum2 = 0
    while (select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            select2 = int(input("고장수리(1)/ 사용문의(2)/ 환불문의(3)/ 기타문의(4)"))
            if(select2 == 1):
                circle_queue_module.enQueue(waiting[0])
                
            elif(select2 == 2):
                circle_queue_module.enQueue(waiting[1])
            elif(select2 == 3):
                circle_queue_module.enQueue(waiting[2]) 
            elif(select2 == 4):
                circle_queue_module.enQueue(waiting[3])   
            else:
                print("잘못입력하셧습니다.")
                continue
            
            print("큐 상태:",circle_queue_module.queue)
            
        elif select == 'E' or select == 'e':
            data = circle_queue_module.deQueue()
            print("추출된 데이터==>",data)
            print("큐 상태 : ",circle_queue_module.queue)
                    
        elif select == 'V' or select == 'v':

            print("귀하의 대기 예상시간은 "+ sum2 + "입니다")
            print("큐 상태 : ",circle_queue_module.queue)
                       
        else:
            print("입력이 잘못 됨")

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택==>")

print("프로그램 종료!")
            
                
            