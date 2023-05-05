def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers: ## 0부터 9까지 돌면서 numbers에 없는 숫자 answer에 더해주기
            answer += i
    return answer
