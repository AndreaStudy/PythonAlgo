import sys
import math
input = sys.stdin.readline

def prime_num(num) :
    if num >= 2 :
        for i in range(2,int(math.sqrt(num))+1) :
            if num % i == 0:
                return False
    return True

T = int(input())

for _ in range(T) :
    N = int(input())
    a, b = N//2 , N//2
    while a > 0 :
        if prime_num(a) == True and prime_num(b) == True :
            print(a, b)
            break
        else :
            a -=1
            b +=1