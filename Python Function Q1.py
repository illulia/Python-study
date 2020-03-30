def is_odd(b): # 입력 받은 숫자의 홀짝을 가려내는 함수
    if b%2 == 1:
        print("a는 홀수 입니다.")
    else:
        print("a는 짝수 입니다.")
    return b
b = is_odd(int(input()))