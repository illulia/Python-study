############################# global value ############################
a = {1:['콜라',[5,600]], 2:['펩시',[5,500]],3:['우유',[5,400]]}
Sold_out = '가 부족합니다. 다른 음료를 골라주세요. 돈을 반환 합니다.'
Error = '오류입니다. 돈을 반환합니다. 다시 넣어주세요.'
No_money = '돈이 부족합니다. 돈을 반환합니다. 다시 넣어주세요.'
Left_money = '를 줍니다. 거스름돈은 %d원 입니다.'

############################# __outPut Function() ##########################
def Classifi(cash,num) :  
    if cash >= a[num][1][1]:
        if a[num][1][0] != 0:
            print(a[num][0] + Left_money % (cash - a[num][1][1]))
            if a[num][1][0] >0:
                a[num][1][0] = a[num][1][0] - 1
        else :
            print(a[num][0] + Sold_out)
    else :
        print(No_money)
