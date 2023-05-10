def solution(s):
    answer = ''
    temp=0
    cnt=0
    # for i in s:
    #     if cnt != 0:
    #         answer+=' '*temp
    #     cnt=0
    #     temp=0
    #     print(i)
#     for j in s:
#         if j==' ':
#             cnt=0
#             temp+=1
#             print(temp)
#         if cnt%2==0:
#             j=j.upper()
#             answer+=j
#         else:
#             j=j.lower()
#             answer+=j
            
#         cnt+=1
#         print(cnt)
#     return answer
def solution(s):
    answer = ''
    new_list = s.split(' ')
    for i in new_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer+= ' '
    return answer[0:-1]