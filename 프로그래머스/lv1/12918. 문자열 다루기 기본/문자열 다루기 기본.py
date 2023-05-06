def solution(s):
    answer=False
    if len(s) == 4 or len(s) == 6:
        answer=s.isdigit()# 숫자만 있다면 True
    print(answer)
    return answer