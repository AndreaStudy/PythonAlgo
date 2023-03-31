import sys
sys.stdin = open('input.txt')

def check(temp):
    if temp in result:
        print(f'#{tc} {temp}')
        return True
    return False

T = int(input())

for tc in range(1, T+1):
    bi = list(input())
    ti = list(input())
    result = set()

    for i in range(len(bi)):
        if bi[i] == '1':
            bi[i] = '0'
            result.add(int(''.join(bi), 2))
            bi[i] = '1'
        else:
            bi[i] = '1'
            result.add(int(''.join(bi), 2))
            bi[i] = '0'

    for i in range(len(ti)):
        if ti[i] == '1':
            ti[i] = '0'
            temp = int(''.join(ti), 3)
            if check(temp):
                break
            ti[i] = '2'
            temp = int(''.join(ti), 3)
            if check(temp):
                break
            ti[i] = '1'
        elif ti[i] == '2':
            ti[i] = '0'
            temp = int(''.join(ti), 3)
            if check(temp):
                break
            ti[i] = '1'
            temp = int(''.join(ti), 3)
            if check(temp):
                break
            ti[i] = '2'
        else:
            ti[i] = '1'
            temp = int(''.join(ti), 3)
            if check(temp):
                break
            ti[i] = '2'
            temp = int(''.join(ti), 3)
            if check(temp):
                break
            ti[i] = '0'

