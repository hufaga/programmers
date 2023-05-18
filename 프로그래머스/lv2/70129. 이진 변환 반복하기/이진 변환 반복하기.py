def solution(x):
    answer = []
    
    cnt = 0
    zero = 0
    
    while x != '1':
        zero = zero + x.count("0")
        x = x.replace("0", "")
        
        x = bin(len(x))[2:]
        
        cnt = cnt + 1
    
    answer = [cnt, zero]
    
    return answer