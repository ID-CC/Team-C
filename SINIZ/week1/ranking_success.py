def preProcess(infos):  # 데이터 전처리를 담당한다.
    info_dict = {}

    # 총 경우의 수 딕셔너리로 정의
    for lang in ['cpp', 'java', 'python', "-"]:
        for job in ['backend', 'frontend', "-"]:
            for career in ['junior', 'senior', "-"]:
                for food in ['chicken', 'pizza', "-"]:
                    info_dict[lang + job + career + food] = []

    for info in infos:
        info = info.split(" ")
        for lang in [info[0], "-"]:
            for job in [info[1], "-"]:
                for career in [info[2], "-"]:
                    for food in [info[3], "-"]:
                        info_dict[lang + job + career + food].append(int(info[4]))

    return info_dict


def solution(infos, queries):
    info_dict = preProcess(infos)

    answer = []

    # 딕셔너리의 키 값 내부의 배열을 정렬
    for key in info_dict.keys():
        info_dict[key].sort()

    # 조건
    for q in queries:
        # 각 쿼리문을 " and " 을 없앤 뒤 공백단위로 split
        # 이렇게하면 0번 인덱스에는 키값과 동일한 문자가 들어가게 됨
        # 1번 인덱스에는 점수
        q = q.replace(" and ", "").split()

        q_score = int(q[1])     # 점수
        q = q[0]                # 키값

        # 
        l = len(info_dict[q])   # 해당 키 값에 있는 int 배열의 길이
        tmp = l                 # 임시

        low, high = 0, l - 1    # low = 0, high = (length - 1)

        while low <= high:      # 바아아로 이진트리탐색
            mid = (low + high) // 2     # 중간값

            if q_score <= info_dict[q][mid]:    # 찾은 중간값보다 쿼리 값이 낮거나 같다면
                tmp = mid                       # temp 변수에 중앙값을 넣고
                high = mid - 1                  # high 변수에 mid - 1을 넣어서
                                                # 이후에 탐색이 중앙값 아래로 탐색되게 한다.
            else:
                low = mid + 1                   # 높다면 중앙값보다 위로 탐색되게한다.

        answer.append(l - tmp)                  # 다시 탐색할 필요없이
                                                # 전체 길이 - 대충 찾은 중앙값을 쌔리면
    return answer                               # 값이 나온다.