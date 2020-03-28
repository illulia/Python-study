while True:
    print("구구단 프로그램을 실행합니다.\n1. 홀수 구구단\n2. 짝수 구구단\n3. 종료")
    dan = int(input("숫자를 입력 하세요: "))
    if dan == 1:
        for j in (3,5,7,9):
            print("%d단\n" % j )
            for i in range(1,10):
                print("%dx%d=%d\n" % (j,i,j*i))
    elif dan == 2:
        for j in (2,4,6,8,):
            print("%d단\n" % j)
            for i in range(1,10):
                print("%dx%d=%d\n" % (j,i,j*i))
    elif dan == 3:
        print("프로그램을 종료 합니다.")   
        break
    else:
        print("잘못 입력 하셨습니다. 1 ~ 3번 숫자를 입력하세요.")   
        continue  