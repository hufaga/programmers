def solution(phone_number):
    answer = ''
    star = len(phone_number)-4
    end = phone_number[-4:]
    answer = '*'*star + end 
    return answer