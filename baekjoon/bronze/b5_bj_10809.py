al_list = [-1] * 26
word = input()
count = 0
for i in word :
    appear = ord(i)-ord('a')
    if al_list[appear] == -1 :
        al_list[appear] = count
    count += 1
for i in al_list :
    print(i, end=" ")