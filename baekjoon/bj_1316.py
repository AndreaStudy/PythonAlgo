import sys
input = sys.stdin.readline

# 단어의 갯수 입력
T = int(input().rstrip())
# 그룹단어의 개수 cnt 생성 기본 값은 입력받은 단어의 갯수
cnt = T
for i in range(T) :
    # 입력받은 단어를 str 타입으로 list에 넣기
    word = list(map(str,input().rstrip()))
    # 입력받은 단어를 순회
    for j in range(len(word)-1) :
        # 다음 단어와 값이 같다면 패스
        if word[j] == word[j+1] :
            pass
        # 다음단어와 값이 같지 않고 이후에 같은 단어가 나온다면
        # 그룹단어가 아니므로 그룹단어 개수 -1하고 break
        elif word[j] in word[j+1:]:
            cnt -=1
            break  
print(cnt)