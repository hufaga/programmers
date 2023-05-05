def solution(seoul):
    answer = ''
    cnt=0
    for i in seoul:
        
        if i == 'Kim':
            return ('김서방은 '+ str(cnt)+'에 있다') ##0번째도 포함하기 위해 cnt 후열 배치
        cnt+=1
    return answer
