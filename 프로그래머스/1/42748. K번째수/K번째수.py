def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        pick = []
        for j in range(commands[i][0], commands[i][1]+1):
            print(j,i)
            pick.append(array[(j-1)])
        pick.sort()
        answer.append(pick[(commands[i][2]-1)])
    
    return answer