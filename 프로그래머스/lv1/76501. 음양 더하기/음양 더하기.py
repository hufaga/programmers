def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]==False:
            absolutes[i] = absolutes[i]*-1 ##signs의 i번째가 false일때 -로 만들어주고 absolutes i번째로 치환
    answer = sum(absolutes) 
    return answer
