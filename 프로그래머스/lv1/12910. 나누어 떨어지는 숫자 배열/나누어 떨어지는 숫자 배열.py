def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor==0: ##나머지가 0일때만 answer에 추가
            answer.append(i)
    answer.sort() ##작은 숫자 먼저
    if not answer: ## answer에 없다면 not false
        answer.append(-1)
    return answer
