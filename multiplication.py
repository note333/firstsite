dan = int(input("몇단을 출력하시겠습니까?"))

def multiple(a):
    for num in range(1, 10):
#        print(a,"x", num, "=",a*num)
        print("{} * {} = {}".format(a, num, a*num))
        
multiple(dan);