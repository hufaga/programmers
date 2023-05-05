def solution(phone_number):
    answer = ''
    star = len(phone_number)-4
    end = phone_number[-4:]
    answer = '*'*star + end  ## star에는 뒤 4개를 제외한 길이만큼 *을 만들고 end에는 phone_number의 뒷자리 4개의 숫자를 더해 문자열 생성
    return answer
