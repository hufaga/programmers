def solution(A,B):
    answer = 0
    # for i in range(len(A)):
    #     if max(A)>max(B):
    #         answer += max(A)*min(B)
    #         A.remove(max(A))
    #         B.remove(min(B))
    #     else:
    #         answer += max(B)*min(A)
    #         A.remove(min(A))
    #         B.remove(max(B))  #시간 복잡도 초과
    if max(A)>max(B):
        A.sort(reverse=True)
        B.sort()
    else:
        A.sort()
        B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i]*B[i]


    return answer
#     def solution(A, B):
    
#     return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])
