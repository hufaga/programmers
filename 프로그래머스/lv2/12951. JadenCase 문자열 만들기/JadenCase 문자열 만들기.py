def solution(s):
    answer = ''
    for i in range(len(s)):
        if i==0 and s[i] != int:
            answer += s[i].upper()
            continue
        if s[i-1] == ' ':
            answer += s[i].upper()
            continue
        else :
            answer += s[i].lower()
    return answer