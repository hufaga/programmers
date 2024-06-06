def solution(my_string, is_prefix):
    answer = 0
    string = []
    for i in range(len(my_string)):
        if my_string[0:i-1] == is_prefix:
            answer += 1
    return answer