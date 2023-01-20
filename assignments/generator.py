def fn_d(N) :
    result = N
    while N != 0 :
        result += N % 10
        N = N // 10
    return result

print(fn_d(91))

def is_selfnumber(M) :
    # M의 generator가 될 수 있는 경우는 1부터 M까지의 숫자 중에 있다
    for i in range(1, M+1) :
        # generator인지 아닌지 판별하는 방법은 숫자 i를 fn_d에 집어 넣었을 때,  그 값이 내가 할당받은 M과 동일하다면,
        # i를 M의 generator라고 할 수 있다.
        # fn_d(91) == 101 : 91은 101의 generator
        if fn_d(i) == M:
            # 하나라도 generator가 있으면 셀프 넘버가 아니므로 셀프 넘버를 판별하는 함수
            # is_selfnumber 함수는 False를 반환하고 종료
            return False
    # 모든 후보군을 모두 출렸했는데 False가 반환되지 않았다면 셀프 넘버가 맞다
    return True

print(is_selfnumber(31))

def is_selfnumber(M) :
    for i in range(1, M+1) :
        # lambda [parameter] : expression
        # 모든 자리수의 합 + 본인을 더한 값
        # while 나머지를 사용해서 더해왔는데...
        # 문자열로 바꿔서 각 자리수를 순회하며 더하기
        # '1234' -> '1','2','3','4'
        # [int(char) for char in 'M'] => [1,2,3,4] + [M]
        # => sum[1,2,3,4,M]
        fn_d = lambda n : sum([int(char) for char in str(n)] + [n])
        if fn_d(i) == M :
            return False
    return True
print(is_selfnumber(30))