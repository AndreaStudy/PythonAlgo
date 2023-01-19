anagram_list = list(input())
result = {}
for i in anagram_list :
    s = ''.join(sorted(i))
    result[s] = result.get(s,[]) + [i]
print(list(result.values()))