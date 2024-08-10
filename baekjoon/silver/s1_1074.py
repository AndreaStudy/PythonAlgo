import sys; input = sys.stdin.readline

N, r, c = map(int, input().split())
result = 0

while N > 1:
    half = 2 ** (N-1)

    if r < half and c < half:
        pass

    elif r < half and half <= c:
        result += half ** 2
        c -= half
        
    elif half <= r and c < half:
        result += half ** 2 * 2
        r -= half
        
    elif half <= r and half <= c:
        result += half ** 2 * 3
        r -= half
        c -= half
        
    N -= 1

if r == 0 and c == 0:
    print(result)
if r == 0 and c == 1:
    print(result + 1)
if r == 1 and c == 0:
    print(result + 2)
if r == 1 and c == 1:
    print(result + 3)