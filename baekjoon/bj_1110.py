number = input()
last = ''
count = 0
first = number
if int(number) <10 :
    number = '0'+number
    first = number
while True :
    temp = int(number[-1]) + int(number[-2])
    number = (number + str(temp)[-1])[-2::]
    last = number
    count +=1
    if first == last :
        break
print(count)