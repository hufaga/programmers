def solution(arr):
    answer = arr
    print(min(arr))
    if len(answer) > 1:
        answer.remove(min(arr))
    else :
        answer = [-1]
    return answer