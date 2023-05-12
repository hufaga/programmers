def solution(arr):
# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
#     for i in range(len(arr)-1):
#         if arr[i] == arr[i+1]:     ## 삭제하는 것은 리스트의 길이가 줄어들어 out of range
#             answer.remove(arr[i])
    answer = []
    for i in arr:
        if answer[-1:] == [i]: continue ##같은 숫자가 있다면 나머지 구문 무시 (중복되는 숫자 제거)
        answer.append(i)
    return answer
