def solution(s, n):
    answer = ''
    sut=0
    mun=''
    for i in s:
        if i == " ":
            answer+=i
            continue
        if 64 < ord(i) <91 and ord(i)+n > 90:
            sut = (ord(i)+n)-26
            mun = chr(sut)
            answer+=mun
            continue
        if 96 < ord(i) < 123 and ord(i)+n > 122:
            sut = (ord(i)+n)-26
            mun = chr(sut)
            answer+=mun
            continue
        sut=ord(i)+n
        mun=chr(sut)
        answer+=mun
    return answer