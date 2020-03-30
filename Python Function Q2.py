def add(*number):
    a = 0
    for c in number:
        a += c
    print("%d" %(a/len(number)))
a =add(20,40,50,70)