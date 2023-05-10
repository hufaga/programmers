def solution(d, budget):
    answer=[]
    d.sort()
    print(d)
    
    for i in d:
        print(i)
        if budget > 0:
            budget=budget - i
            if budget >= 0:
                answer.append(i)
                print(answer)
            
    return len(answer)