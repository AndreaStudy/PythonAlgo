import calendar

year = int(input("연도를 입력해주세요: "))

# 윤년 판별 함수 isleap에 사용자가 입력한 값을 인자로 전달
# 만약 윤년이라면, 반복문 실행
while calendar.isleap(year):
	print("윤년입니다. 연도를 다시 입력해주세요.")
	# 다시 값을 입력받는다.
	year = int(input("연도를 입력해주세요: "))
# 입력한 년도에 해당하는 달력을 출력해준다.
print(calendar.calendar(year))

month = int(input("'월'을 입력해주세요: "))

day = int(input("'일'을 입력해주세요."))

# 년, 월, 일을 입력하면 요일에 해당하는 번호를 출력한다.
weekday_num = calendar.weekday(year, month, day)

# 월요일이 0으로 설정되어 있으므로, weekday_num이 False면
# 월요일에 대한 경고를 출력한다.
if not weekday_num:
	print("경고 월요일입니다.")

# 각 요일에 대한 번호를 dict로 작성하고
week_dict = {0: "월요일", 1: "화요일", 2: "수요일",
                3: "목요일", 4: "금요일", 5: '토요일', 6: '일요일'}

# 입력받은 년월일과 계산되어 나온 요일을 출력한다.
date_dict = {"년": year, "월": month,
                "일": day, "요일": week_dict[weekday_num]}
print(date_dict)
