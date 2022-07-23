def solution(dartResult):
    answer = 0
    
    dartResult = list(dartResult)
    history = [0,0,0]
    number = 0
    flag = False
    idx = 0
    for i in dartResult:
        if chr(57) >= i >= chr(48):
            if flag:
                number = 10
            else:
                number = int(i)
            flag = True
                
            
        else:
            if i == 'S':
                answer = number
                history[idx] = answer
                idx += 1
                
            elif i == 'D':
                answer = number ** 2
                history[idx] = answer
                idx += 1
                
            elif i == 'T':
                answer = number ** 3
                history[idx] = answer
                idx += 1
                
            if i =='*':
                if idx >= 1:
                    history[idx-1] *= 2
                    history[idx-2] *= 2
                else:
                    history[idx-1] *= 2
                
                pass
            elif i == '#':
                history[idx-1] *= -1
                    
        
                
            flag = False
    print(history)
    return sum(history)