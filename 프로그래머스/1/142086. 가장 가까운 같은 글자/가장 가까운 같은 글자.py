# 처음 나온것을 어떻게 구분 할 것인가
    # 리스트를 만들어서 리스트 안에 있는 문자와 현재 문자를 비교
# 나왔다면 몇 번째 앞에 나온 것을 어떻게 찾을 수 있나
    # enumerate를 사용해 index를 같이 추출해 현재 index 값과 past 리스트의 인덱스 값을               연산

def solution(s):
    answer = []
    past = {}
    for idx, i in enumerate(s):
        if i not in past:
            past[i] = [idx]
            answer.append(-1)
        else:
            answer.append(idx-max(past[i]))
            past[i].append(idx)
            


    return answer