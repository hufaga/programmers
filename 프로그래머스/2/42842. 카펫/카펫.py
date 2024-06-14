# def solution(brown, yellow):
#     answer = []
#     size = brown + yellow  
#     print(size)
#     for i in range(size):
#         for j in range(size):
#             if i * j == size and i >= j:
#                 if (i-2) * (j-2) == yellow:
#                     answer.append(i)
#                     answer.append(j)
#     # return answer



def solution(brown, yellow):
    answer = []
    size = brown + yellow  
    print(size)
    for i in range(1,yellow+1):
        if yellow % i == 0:
            width = yellow // i
            height = i
            if (width+2) * (height+2) == size:
                answer.append(width+2)
                answer.append(height+2)
                break
    return answer