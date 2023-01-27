# 설탕배달 N킬로그램
# 3킬로그램 봉지 + 5킬로그램 봉지
# 최대한 적은 봉지
# ex) 18키로 배달할때 3키로 6개도 되지만
# 5키로 3개와 3키로 1개를 배달하면 더 작은 봉지 배달
# 정확하게 설탕을 N키로 배달해야할 때 봉지 몇개를 가져가면되는지?
# 입력은 키로수 출력은 봉지 개수
def kg_cnt(kg) :
    cnt = 0
    if kg % 5 == 0:
        cnt = kg // 5
        return cnt
    else :
        for i in range(1, (kg//3)+1) :
            f_kg = kg-3*i
            cnt +=1
            if f_kg % 5 == 0 :
                cnt += (f_kg//5)
                return cnt
            f_kg = kg
        return -1

if __name__ == "__main__" :
    print(kg_cnt(int(input())))

