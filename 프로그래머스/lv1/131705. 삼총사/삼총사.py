import itertools
def solution(number):
    answer = 0
    for i in itertools.combinations(number,3): ##itertools.combinations를 사용하면 입력받은 데이터의 모든 경우의 수를 반환 
        if sum(i)==0:
            answer+=1
        
    return answer
