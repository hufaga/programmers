def solution(sizes):
    # answer = 0
    # lis = []
    # j=0
    # for i in sizes:
    #     lis.append(sum(i))
    # j=max(lis).index
    # answer = sizes[j]
    
    answer = max(max(x) for x in sizes) * max(min(y) for y in sizes)  ##sizes 중에서 큰것들 중 가장 큰것 과 작은것들 중 가장 큰 것을 곱한 값을 return
    return answer
