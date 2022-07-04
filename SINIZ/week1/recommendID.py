import re

def subSpecialWord(id):                 # 특수문자를 제거
    pattern = r"[^a-z0-9-_.]+"          # 알파벳, 숫자, ., _, - 문자를 제외하고 모두 제거한다
    ne = re.sub(pattern, "", id)
    return ne

def replaceDots(id):                    # 연속된 점들을 제거
    pattern = r"[.]{2,1000}"            # 점이 2번 이상, 1000번 이하 반복되는 점을 점 하나로 대체한다.                    
    ne = re.sub(pattern, ".", id)
    return ne 

def dropDotsInTips(id):                 # 끝부분 점 제거

    """수정"""
    if len(id) == 0:
        return id

    flag = [False, False]               # [앞,뒤]로 점이 있는지 확인하는 플래그
    if(id[0] == "."):
        flag[0] = True
    if(id[-1] == "."):
        flag[1] = True
        
    if flag[0] and flag[1]:             # [앞, 뒤]에 점이 있다면 각각 str 인덱싱을 통해 리턴한다.
        return id[1:len(id)-1]
    elif flag[0]:
        return id[1:]
    elif flag[1]:
        return id[:len(id)-1]
    else:                               # 없음 말고 ㅋ
        return id

def stripStr(id):                       # 문자 최종 처리단
    if len(id) == 0:                    # 문자 길이가 0이면 그냥 aaa를 넣는다.
            return "aaa"                # a를 넣으라곤하지만 어차피 빈 문자에 a를 넣어도 결과적으로 aaa가 되야하기 때문.

    if len(id) <= 2:                    # 문자 길이가 2 이하면 가장 끝 문자를 
        new_char = id[-1]
        new_id = id
        while (len(new_id) < 3):        # 문자열의 길이가 3 이상이 될때까지 붙인다. 
            new_id += new_char          # ex ) ab => abb, 3 => 333
        return new_id
            
    if len(id) >= 16:                   # 문자열의 길이가 16 이상이면 15까지의 문자열만 리턴한다
        return id[:15]
    else:                               # 아님 말고 ㅋ
        return id 
    
def solution(new_id):                   
                                        # 문자열을 소문자로 바꾸고, 특수문자를 제거한 뒤, 연속된 점을 제거한다.
    ne = replaceDots(subSpecialWord(new_id.lower())) 

    while True:                         # 한무 반복문
        ne = dropDotsInTips(ne)         # 끝부분에 점이 있는지 확인하고 제거한다.
        ne = stripStr(ne)               # 문자열의 길이에 따라 적절한 처리를 실시한다.
        if(ne[-1]) != ".":              # 만약 문자열의 맨 뒤에 점이 없다면 반복문을 종료한다.
            break
    return ne
