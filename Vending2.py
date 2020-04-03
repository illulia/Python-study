######################## global value ############################
a = {1:['콜라',[1,600]], 2:['펩시',[1,500]],3:['우유',[1,400]]}
Sold_out = '가 부족합니다. 다른 음료를 골라주세요. 돈을 반환 합니다.'
Error = '오류입니다. 돈을 반환합니다. 다시 넣어주세요.'
No_money = '돈이 부족합니다. 돈을 반환합니다. 다시 넣어주세요.'
Left_money = '를 줍니다. 거스름돈은 %d원 입니다.'

######################## __outPut Function() ##########################
def outPut(money,num):  
    if money >= a[num][1][1]: 
        if a[num][1][0] != 0:
            a[num][1][0] = a[num][1][0]-1
            print(a[num][0] + Left_money % (money - a[num][1][1]))
        else:
            print(a[num][0] + Sold_out)
    else :
        print(No_money)

######################## mainForm_menu #############################
while True:
    money = int(input("돈을 넣어 주세요."))
    print('투입금액 : %d원' %money)
    if money >= 400:
        print("콜라 1번, 펩시 2번, 우유 3번")
        select = int(input("음료를 골라주세요."))
        for i in range(1,4):
            if i == select:
                outPut(money,select)
                break
        if select > 3:
            print(Error)
    else: #돈을 400원 보다 적게 넣었을떄
        print("돈이 부족합니다. 최소한 %d원은 더 넣어주세요." % (400 - money))
    if a[1][1][0]==0 and a[2][1][0]==0 and a[3][1][0] == 0: #음료가 없을 경우
        print("음료가 없습니다. 자판기를 종료합니다.")
        break