import Vending
############################# mainForm_menu #############################
while True:
    money = int(input("돈을 넣어 주세요."))
    print('투입금액 : %d원' %money)
    if money >= 400 :
        print("콜라 1번, 펩시 2번, 우유 3번")
        select = int(input("음료를 골라주세요."))
        for i in range(1,4):
            if i == select:
                Vending.Classifi(money,select)
        if select > 3:
            print(Vending.Error)
    else: #돈을 400원 보다 적게 넣었을떄
        print("돈이 부족합니다. 최소한 %d원은 더 넣어주세요." % (400 - money))
    if Vending.a[1][1][0] < 1 and Vending.a[2][1][0] < 1 and Vending.a[3][1][0] < 1: #음료가 없을 경우
        print("음료가 없습니다. 자판기를 종료합니다.")
        break