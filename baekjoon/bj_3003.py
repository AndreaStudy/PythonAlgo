count = list(map(int,input().split()))
chess = [1,1,2,2,2,8]
fix = []
for i in range(len(count)) :
    fix_num =0
    if count[i] == chess[i] :
        fix.append(0)
    elif count[i] > chess[i] :
        fix_num = chess[i] - count[i]
        fix.append(fix_num)
    else :
        fix_num = chess[i] - count[i]
        fix.append(fix_num)
    print(f'{fix[i]}', end=" ")