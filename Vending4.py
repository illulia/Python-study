import Vending
############################# mainForm_menu #############################
while True:
    money = int(input("돈을 넣어 주세요."))
    if money == 0:
        password = int(input("관리자 모드를 실행합니다.\n비밀번호를 입력해주세요 : "))
        if password == Vending.code:
            print(Vending.menu)
            drink = input()
            amount = input()
            Vending.manager(int(drink),int(amount))
    if money >= 400 :
        print('투입금액 : %d원' %money)
        print(Vending.menu)
        select = int(input("음료를 골라주세요."))
        for i in range(1,4):
            if i == select:
                Vending.Classifi(money,select)
        if select > 3:
            print(Vending.Error)
    elif money != 0 : #돈을 400원 보다 적게 넣었을떄
        print("돈이 부족합니다. 최소한 %d원은 더 넣어주세요." % (400 - money))
    if Vending.a[1][1][0] < 1 and Vending.a[2][1][0] < 1 and Vending.a[3][1][0] < 1: #음료가 없을 경우
        print("음료가 없습니다. 자판기를 종료합니다.") 
        break