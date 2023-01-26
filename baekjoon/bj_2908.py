N1, N2 = list(map(str, input().split()))

reverse_N1 = list(reversed(N1))
reverse_N2 = list(reversed(N2))

new_N1 = ''
new_N2 = ''
for i in reverse_N1 :
    new_N1 += i
for i in reverse_N2 :
    new_N2 += i

if int(new_N1) > int(new_N2) :
    print(new_N1)
else :
    print(new_N2)