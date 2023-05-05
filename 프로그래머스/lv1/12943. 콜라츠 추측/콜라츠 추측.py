def solution(num):
    cnt=0
    while True:
        if num==1:
            break  
        if num%2==0: ## 짝수 홀수 구별 
            num=num//2
            cnt+=1  ## 실행될때마다 카운트
        else:
            num=num*3+1
            cnt+=1
        if cnt >= 500: ## 500회 이상 반복시 -1 리턴
            return -1
        
    return cnt
