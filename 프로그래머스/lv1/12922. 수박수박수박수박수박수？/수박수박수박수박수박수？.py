def solution(n):
    answer = ''
    temp = '수박' * (n//2+1) ##홀수 일때를 위해
    answer=temp[:n] 
    return answer
