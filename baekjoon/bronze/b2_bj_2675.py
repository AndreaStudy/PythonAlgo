import sys

T = int(input())

for test_case in range(T) :
    N, M = map(str, sys.stdin.readline().split())
    for i in M :
        print(i*int(N), end="")
    print()
