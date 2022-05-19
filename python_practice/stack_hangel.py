import stack_module

if __name__ == "__main__":
    road = ["주황","초록","빨강","보라","청록","민트"]
    
    print("과자집에 가는길 : ", end='')
    for i in road:
        stack_module.push(i)
        print(i, end="-->")

    print("과자집")    
    
    print("우리집에 오는길 : ", end='')
    while True:
        road = stack_module.pop()
        if road == None:
            break
        print(road, end="-->")

    print("우리집")  
          
