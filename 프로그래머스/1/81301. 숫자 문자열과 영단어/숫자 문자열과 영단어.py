def solution(s):
    answer = 0
    numeric = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for idx, i in enumerate(numeric):
        if i in s:
            s = s.replace(i,str(idx))
    answer=int(s) ## 맨 마지막에 치환하는 이유는 문자열은 int로 형변환 불가능
    
    return answer