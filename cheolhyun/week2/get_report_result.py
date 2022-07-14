"""
  - id_list의 길이가 N일 때, NxN 크기의 2차원 리스트 arr을 선언
    - i번째 유저가 j번째 유저를 신고한 경우, arr[i][j]에 1을 할당.
  - arr 리스트에서 k번 이상 신고된 유저를 탐색한다.
  - 탐색한 유저를 신고한 이력이 있는 i번째 유저에 대해, answer[i]의 값을 ++ 처리한다.
"""


def solution(id_list, report, k):
    id_list_len = len(id_list)
    answer = [0] * id_list_len
    arr = [[0] * id_list_len for _ in range(0, id_list_len)]  # 2차원 리스트

    for condition in report:
        reporter, respondent = condition.split()  # ["muzi frodo"] => "muzi", "frodo" 로 할당해준다.
        reporter_idx = id_list.index(reporter)  # 신고자의 index
        respondent_idx = id_list.index(respondent)  # 피신고자의 index
        arr[reporter_idx][respondent_idx] = 1  # 신고자가 신고한 유저의 index를 1로 변경해준다.

    for i in range(0, id_list_len):
        count = 0
        for j in range(0, id_list_len):
            if arr[j][i] == 1:  # 신고 당했는지 체크.
                count += 1

        if count >= k:  # k번 이상 신고당한 사람
            for j in range(0, id_list_len):
                if arr[j][i] == 1:  # k번 이상 신고당한 사람을 신고했는지 체크.
                    answer[j] += 1  # 이메일 발송 횟수 1 증가. 

    return answer


if __name__ == "__main__":
    print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
    # solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)


"""
프로그래머스 "다른사람의 풀이" 중, 
set()을 사용한 깔끔한 풀이가 있어서 첨부했습니다.

def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
    
"""