cola = 5 #가격은 600원
pepsi = 5 #가격은 500원
milk = 5 # 가격은 400원
while True:
    money = int(input("돈을 넣어 주세요."))
    if money >= 600:
        print("콜라 1번, 펩시 2번,우유 3번")
        select = int(input("음료를 골라주세요."))
        if select == 1:
            cola = cola -1
            if cola != 0:
                print("콜라를 줍니다. 거스름돈은 %d원입니다." % (money - 600))
            else:
                print("콜라가 부족합니다. 다른 음료를 골라주세요. 돈을 반환 합니다.")
        elif select == 2:
            pepsi = pepsi -1
            if pepsi != 0:
                print("펩시를 줍니다. 거스름돈은 %d원입니다." % (money - 500))
            else:
                print("펩시가 부족합니다. 다른 음료를 골라주세요. 돈을 반환 합니다.")
        elif select == 3:
            milk = milk -1
            if milk != 0:
                print("우유를 줍니다. 거스름돈은 %d원입니다." % (money - 400))
            else:
                print("우유가 부족합니다. 다른 음료를 골라주세요. 돈을 반환 합니다.")
        else:
            print("오류입니다. 돈을 반환합니다. 다시 넣어주세요")
    elif money >= 500:
        print("펩시 1번,우유 2번")
        select = int(input("음료를 골라주세요."))
        if select == 1:
            pepsi = pepsi -1
            if pepsi != 0:
                print("펩시를 줍니다. 거스름돈은 %d원입니다." % (money - 500))
            else:
                print("펩시가 부족합니다. 다른 음료를 골라주세요. 돈을 반환 합니다.")    
        elif select == 2:
            milk = milk -1
            if milk != 0:
                print("우유를 줍니다. 거스름돈은 %d원입니다." % (money - 400))
            else:
                print("우유가 부족합니다. 다른 음료를 골라주세요. 돈을 반환 합니다.")
        else:
            print("오류입니다. 돈을 반환합니다. 다시 넣어주세요")
    elif money >= 400:
        print("우유 1번")
        select = int(input("음료를 골라주세요."))
        if select == 1:
            milk = milk -1
            if milk != 0:
                print("우유를 줍니다. 거스름돈은 %d원입니다." % (money - 400))
            else:
                print("우유가 부족합니다. 다른 음료를 골라주세요. 돈을 반환 합니다.")
        else:
            print("오류입니다. 돈을 반환합니다. 다시 넣어주세요")
    elif money < 400:
        print("돈이 부족합니다. 최소한 %d원은 더 넣어주세요." % (400 - money))
    elif pepsi == cola == milk == 0:
        print("음료가 없습니다. 자판기를 종료합니다")
        brek

       
            






