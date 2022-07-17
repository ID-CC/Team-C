"""테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (164.19ms, 52.8MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.83ms, 10.4MB)
테스트 7 〉	통과 (2.26ms, 10.8MB)
테스트 8 〉	통과 (1.74ms, 11.1MB)
테스트 9 〉	통과 (65.47ms, 29.8MB)
테스트 10 〉	통과 (54.13ms, 29.7MB)
테스트 11 〉	통과 (158.80ms, 52.9MB)
테스트 12 〉	통과 (0.23ms, 10.4MB)
테스트 13 〉	통과 (0.21ms, 10.3MB)
테스트 14 〉	통과 (47.06ms, 25.8MB)
테스트 15 〉	통과 (74.81ms, 38.4MB)
테스트 16 〉	통과 (0.14ms, 10.2MB)
테스트 17 〉	통과 (0.21ms, 10.3MB)
테스트 18 〉	통과 (0.37ms, 10.4MB)
테스트 19 〉	통과 (0.57ms, 10.3MB)
테스트 20 〉	통과 (46.40ms, 25.8MB)
테스트 21 〉	통과 (83.04ms, 38.2MB)
테스트 22 〉	통과 (0.01ms, 10.3MB)
테스트 23 〉	통과 (0.01ms, 10.3MB)
테스트 24 〉	통과 (0.01ms, 10.2MB)"""


# 놀랍게도 이 문제가 1시간 반. 광고 삽입에 비비는 매직
def solution(id_list, report, k):
    id_dic = {}
    answer = []
    count = {}
    
    # 중복제거
    report = set(report)
    
    # 자료를 취합할 딕셔너리와, 카운트 딕셔너리 내부 선언 
    for i in id_list:
        id_dic[i] = {}
        count[i] = 0
    
    # 자료 딕셔너리 세부값 선언
    for i in report:
        [er,ed] = i.split()
        id_dic[ed][er] = 1
    
    # 자료 딕셔너리 2중 탐색  
    # 내부 구조의 길이가 k보다 크다면 (신고자가 k 이상이라면)
    # 그때마다 카운트딕셔너리 내 신고자의 이름에 1씩 더한다. 
    for i in id_dic:
        for j in id_dic[i]:
            if len(id_dic[i]) >= k:        
                count[j] += 1

    # 더해진 값을 answer에 넣어 먹어보세요 ^^7
    for i in count:
        answer.append(count[i])
    return answer