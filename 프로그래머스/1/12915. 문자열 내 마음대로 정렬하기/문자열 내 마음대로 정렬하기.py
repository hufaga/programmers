# def solution(strings, n):
#     answer = []
#     dic = {1:'뭐고'}
#     for i in range(len(strings)):
#         print(strings[i][n])
#         dic[i+1] = strings[i][n]
#     dic = sorted(dic.items(), key=lambda x: x[1] )
#     print(dic)
#     for i in range(len(dic)):
#         j = dic[i][0]
#         answer.append(strings[j-1])
#     return answer

def solution(strings, n):
    strings.sort()
    print(strings)
    return sorted(strings, key=lambda x: x[n])