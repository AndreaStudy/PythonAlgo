import bisect

a = bisect.bisect_left([1, 2, 3, 4, 5, 6], 8)
print(a)
# cnt = 0
# zcnt = 0


# def check(s):
#     global cnt, zcnt
#     cnt += 1
#     length = 0
#     for seq in s:
#         if seq == '0':
#             zcnt += 1
#         else:
#             length += 1
#     return bin(length)[2:]


# def solution(s):
#     global cnt, zcnt
#     answer = [cnt, zcnt]
#     if s == '1':
#         return answer
#     else:
#         return solution(check(s))


# print(solution("110010101001"))
