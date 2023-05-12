def solution(sizes):
    # answer = 0
    # lis = []
    # j=0
    # for i in sizes:
    #     lis.append(sum(i))
    # j=max(lis).index
    # answer = sizes[j]
    
    answer = max(max(x) for x in sizes) * max(min(y) for y in sizes)
    return answer