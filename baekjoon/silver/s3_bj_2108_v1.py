import sys
input = sys.stdin.readline

T = int(input())
array = [int(input()) for _ in range(T)]
array.sort()

print(round(sum(array)/T))

cen_num = array[T//2]
print(cen_num)

set_array = list(set(array))
set_list = []
fre_num = 0
for i in set_array :
    set_list.append([i, array.count(i)])
set_list.sort(key=lambda x : x[0], reverse=True)
if len(set_list) == 1 :
    print(set_list[0][0])
elif set_list[0][1] == set_list[1][1] :
    print(set_list[1][0])
else :
    print(set_list[0][0])

if array[0] - array[-1] == 0 :
    print(0)
else :
    print((array[-1]-array[0]))