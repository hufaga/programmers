def solution(n):
    answer = n
    while True:
            answer+=1
            cnt_i = 0
            cnt_j = 0
            for i in bin(answer):
                if i=='1':
                    cnt_i+=1
            for j in bin(n):
                if j=='1':
                    cnt_j+=1
            if cnt_i==cnt_j:
                break
    return answer