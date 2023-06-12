def solution(s):
    answer = 0
    st = []
    for i in s:
        if len(st)==0:
            st.append(i)
            #print(st)
        else:
            if st[-1] == i :
                
                #print("pop 하기 전")
                #print(st)
                st.pop()
                #print("pop 한 후")
                #print(st)
            else:
                st.append(i)
                #print('앞뒤가 같지 않은 경우')
                #print(st)
    if len(st)==0:
        answer = 1
    return answer