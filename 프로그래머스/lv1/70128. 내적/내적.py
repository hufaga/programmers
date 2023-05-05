def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i] ## a와 b의 i번째 곱하고 answer에 a의 길이만큼 더해주기 
    return answer
