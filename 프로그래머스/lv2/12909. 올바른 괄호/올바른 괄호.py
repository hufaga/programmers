def solution(s):
    answer = True
    lcnt=0
    rcnt=0
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    if s[0] == ')'or s[len(s)-1] =='(':
        answer=False
    for i in range(len(s)):
        if s[i]=='(':
            lcnt+=1
        else:
            rcnt+=1
        if rcnt > lcnt:
            answer=False
    print(lcnt,rcnt)
    if lcnt != rcnt:
        answer=False
    
    return answer