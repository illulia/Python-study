a = 1 #0부터 1000까지의 모든 3의 배수를
b = 0
while a <= 1000:
    if a % 3 == 0:
        b += a
    a += 1
print(b)
