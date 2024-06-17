def solution(food):
    answer = ''
    for i in range(len(food)):
        if int(food[i]) >= 2:
            answer += str(i) * (int(food[i]) // 2)
        second = ''.join(reversed(answer))
    answer = answer + '0' + second
    return answer