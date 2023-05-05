def solution(s):
    answer = ''
    if len(s)%2==0:
        answer= s[len(s)//2-1]+s[len(s)//2] ## 짝수일땐 목의 전 str까지 포함
    else:
        answer = s[len(s)//2]
    
    return answer
