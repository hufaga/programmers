def solution(phone_number):
    answer = ''
    for idx,i in enumerate(phone_number):
        if idx < (len(phone_number)-4):
            answer+='*'
        else:
            answer+=i
    return answer