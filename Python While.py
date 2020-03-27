a = {'cola':[5,'콜라'], 'pepsi':[5,'펩시'],'milk':[5,'우유']}
Sold_out = '가 부족합니다. 다른 음료를 골라주세요. 돈을 반환 합니다'
Error = '오류입니다. 돈을 반환합니다. 다시 넣어주세요.'
while True:
    money = int(input("돈을 넣어 주세요."))
    print('투입금액 : ' + str(money) + '원')
    if money >= 600:
        print("콜라 1번, 펩시 2번, 우유 3번")
        select = int(input("음료를 골라주세요."))
        if select == 1:
            if a['cola'][0] != 0:
                a['cola'][0] = a['cola'][0]-1
                print("콜라를 줍니다. 거스름돈은 %d원 입니다." % (money - 600))
            else:
                print(a['cola'][1] + Sold_out)
        elif select == 2:
            if a['pepsi'][0] != 0:
                a['pepsi'][0] = a['pepsi'][0]-1
                print("펩시를 줍니다. 거스름돈은 %d원 입니다." % (money - 500))
            else:
                print(a['pepsi'][1] + Sold_out)
        elif select == 3:
            if a['milk'][0] != 0:
                a['milk'][0] = a['milk'][0]-1
                print("우유를 줍니다. 거스름돈은 %d원 입니다." % (money - 400))
            else:
                print(a['milk'][1] + Sold_out)
        else:
            print(Error)
    elif money >= 500:
        print("펩시 1번, 우유 2번")
        select = int(input("음료를 골라주세요."))
        if select == 1:
            if a['pepsi'][0] != 0:
                a['pepsi'][0] = a['pepsi'][0]-1
                print("펩시를 줍니다. 거스름돈은 %d원 입니다." % (money - 500))
            else:
                print(a['pepsi'][1] + Sold_out)    
        elif select == 2:
            if a['milk'][0] != 0:
                a['milk'][0] = a['milk'][0]-1
                print("우유를 줍니다. 거스름돈은 %d원 입니다." % (money - 400))
            else:
                print(a['milk'][1] + Sold_out)
        else:
            print(Error)
    elif money >= 400:
        print("우유 1번")
        select = int(input("음료를 골라주세요."))
        if select == 1:
            if a['milk'][0] != 0:
                a['milk'][0] = a['milk'][0]-1
                print("우유를 줍니다. 거스름돈은 %d원 입니다." % (money - 400))
            else:
                print(a['milk'][1] + Sold_out)
        else:
            print(Error)
    elif money < 400:
        print("돈이 부족합니다. 최소한 %d원은 더 넣어주세요." % (400 - money))
    if a['cola'][0] == a['pepsi'][0] == a['milk'][0] == 0:
        print("음료가 없습니다. 자판기를 종료합니다.")
        break

       
            






