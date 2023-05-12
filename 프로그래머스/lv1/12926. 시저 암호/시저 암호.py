def solution(s, n):
    answer = ''
    sut=0
    mun=''
    for i in s:
        if i == " ":                          ## 공백은 공백으로 출력 
            answer+=i
            continue
        if 64 < ord(i) <91 and ord(i)+n > 90: ## 대문자일때 ../ isupper 쓸 걸 그랬다..
            sut = (ord(i)+n)-26
            mun = chr(sut)
            answer+=mun
            continue                          ## ascii code가 대문자 범위를 over하지 않을 때 나머지 구문 무시 
        if 96 < ord(i) < 123 and ord(i)+n > 122: ## 소문자일때
            sut = (ord(i)+n)-26
            mun = chr(sut)
            answer+=mun
            continue
        sut=ord(i)+n
        mun=chr(sut)
        answer+=mun
    return answer
