import sys
input = sys.stdin.readline

word = input().rstrip()
cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro_alpha :
    word = word.replace(i, '*')
print(len(word))