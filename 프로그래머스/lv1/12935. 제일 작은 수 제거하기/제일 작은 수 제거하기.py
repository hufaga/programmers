def solution(arr):
    answer = []
    
    
    if len(arr) == 1: ## 숫자가 하나밖에 없다면 -1리턴
        answer.append(-1)
    else: ## arr에 두개 이상 담고 있다면 제일 작은 숫자 제거
        arr.remove(min(arr))
        answer = arr
    return answer
