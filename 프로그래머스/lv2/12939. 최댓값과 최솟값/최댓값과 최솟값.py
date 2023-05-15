def solution(s):
    answer = ''
    ans=[]
    ns = s.split(' ')
    print(ans)
    for i in ns:
        ans.append(int(i))
    answer = str(min(ans)) + ' ' + str(max(ans))
        
    return answer