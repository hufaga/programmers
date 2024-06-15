def solution(numbers):
    answer = []
    numbers.sort()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum = numbers[i] + numbers[j]
            print(sum)
            if sum not in answer:
                answer.append(sum)
                print(answer,'answer')
    answer.sort()
    return answer