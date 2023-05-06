def solution(price, money, count):
    answer = 0
    cost=0
    for i in range(1,count+1):
        cnt_price=price*i
        cost+=cnt_price

    answer = money - cost
    if answer>0:
        return 0
    else:
        answer*=-1
    return answer