def solution(t, p):
    n = len(t)
    answer = 0
    
    for i in range(n):
        if len(t[i:i+len(p)]) == len(p):
            if int(t[i:i+len(p)]) <= int(p):
                answer += 1
                
    return answer