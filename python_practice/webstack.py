import time
import webbrowser
import stack_module


if __name__ == "__main__":
    urls = ['naver.com','daum.net','nate.com','google.com']
    
    for url in urls:
        stack_module.push(url)
        webbrowser.open('http://'+url)
        print(url, end = '-->')
        time.sleep(1)
    print("방문 종료")
    time.sleep(5)
    
    while True:
        url = stack_module.pop()
        if url == None:
            break
        webbrowser.open('http://'+url)
        print(url, end= '-->')
        time.sleep(1)
    print("방문 종료")    