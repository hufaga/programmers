def solution(s):
    answer = ''
    new_list = s.split(' ')
    for i in new_list:            
        for j in range(len(i)):         
            if j % 2 == 0:               
                answer += i[j].upper()      ## 짝수번째는 대문자로  
            else:
                answer += i[j].lower()      ## 홀수번째는 소문자로 
        answer+= ' '                        
    return answer[0:-1]
