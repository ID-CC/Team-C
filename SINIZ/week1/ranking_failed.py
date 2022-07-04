""" 
정확도는 만점이나,,, 효율이 0점!
이유는 바로 무지성 O(n²) 알고리즘 때문!
이번 버전에서는 점수에따라 값을 정렬하지도 않았기에 쿼리문과 데이터가 많아지면 개핵느려진다.
개선을 어떻게 했는지는 개선버전에서 서술
"""

def preProcess(info, query):        # 데이터 전처리를 담당한다.
    new_info = []
    new_query = []
    for i in info:                            
        new_info.append(i.split())                      # 데이터를 공백문자단위로 split
    #     new_info[-1][4] = int(new_info[-1][4])        # 마지막 데이터는 integer 타입으로 변환한다.
    # new_info.sort(key=lambda x:int(x[4]))             # 저장된 데이터를 코딩 점수단위로 정렬한다.
    
    for i in query:         
        new_query.append(i.split())                     # 데이터를 공백문자단위로 split
        del new_query[-1][1], new_query[-1][2], new_query[-1][3]  # 글자 사이사이에 들어간 and를 제거 ^^
        
    return new_info, new_query
        
def compare(a, b):      # 쿼리문과 데이터가 같다면 TRUE, 또는 쿼리문이 - 이여도 TRUE 리턴
    if a==b or a=='-':
        return True
    else:               # 아님 말고
        return False
    
def scoreCompare(a,b):  #점수가 쿼리문에 있는 것 이상이라면 TRUE 리턴
    if int(b)>=int(a):
        return True
    else:
        return False
        
def solution(info, query):
    
    info, query = preProcess(info, query)       # 데이터 전처리
    
    result = []
    for i in query:                             # 무지성
        cnt = 0
        for j in info:                          # 반복문
            if compare(i[0], j[0]) and compare(i[1], j[1]) and compare(i[2], j[2]) and compare(i[3], j[3]) and scoreCompare(i[4], j[4]):    # 값 비교
                cnt+=1        
                
        result.append(cnt)
    
    return result