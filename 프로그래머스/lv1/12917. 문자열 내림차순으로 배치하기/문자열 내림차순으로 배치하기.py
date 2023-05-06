def solution(s):
    answer = ''
    ls = sorted(list(s), reverse=True) ## 문자열 정렬시 대문자가 맨앞으로 내림차순 reverse
    ls=''.join(ls) ## 
    answer = ls
    return answer