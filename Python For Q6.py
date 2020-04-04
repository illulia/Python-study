numbers = [1, 2, 3, 4, 5] #리스트 내포를 이용해 홀수만 출력하기 
result = [i*2  for i in numbers if i % 2 == 1]
print(result)