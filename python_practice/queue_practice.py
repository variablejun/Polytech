
import circle_queue_module

if __name__ == "__main__":
    waiting = ["은비","사쿠라","원영","민주","뱅준"]
    print("대기 줄 상태 : ",end=" ")
    
    for i in waiting:
        circle_queue_module.enQueue(i)
        
    print(circle_queue_module.queue);   
 # 대기 줄 상태 :  [None, '은비', '사쿠라', '원영', '민주', '뱅준', None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        
    while(True):
        fifo = circle_queue_module.deQueue()
        if(fifo == None):
            print("식당 영업 종료!")
            break
        print(fifo + "님 식당에 들어감")
        
        print(circle_queue_module.queue);
        print()
        

        
         

    