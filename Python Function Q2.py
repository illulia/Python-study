def add(*number): #입력받은 숫자를 모두 더해서 평균을 내는 함수
    a = 0
    for c in number:
        a += c
    print("%d" %(a/len(number)))
add(20,40,50,70)