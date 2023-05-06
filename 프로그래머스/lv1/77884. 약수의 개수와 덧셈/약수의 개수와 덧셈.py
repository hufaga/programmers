def solution(left, right):
    answer = 0
    
    for i in range(left,right+1):
        
        if i**0.5==int(i**0.5): ##제곱근이 정수로 나누어 떨어지면 약수의 개수가 홀수
            answer-=i
        else:
            answer+=i
    return answer
