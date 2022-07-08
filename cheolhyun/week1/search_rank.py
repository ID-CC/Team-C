# 1. 입력 info에서 발생할 수 있는 모든 경우의 수를 만든다.
#   1.1. 경우의 수를 key로, 지원자의 점수를 value로 하는 dictionary를 생성하여 미리 저장해놓는다.
# 2. 이분탐색을 통해, 탐색 시간울 단축시킨다.

from collections import defaultdict  # Dictionary
from bisect import bisect_left  # 이분 탐색
from itertools import combinations  # 조합


# 데이터 전처리(informatoin에서 나올 수 있는 모든 경우의 수를 딕셔너리에 저장한다.(메모이제이션))
def dataProcess(information):
    dic = defaultdict(list)
    for info in information:
        info = list(info.split())  # ['java', 'backend', 'junior', 'pizza', 150]
        pick = info[:-1]  # ['java', 'backend', 'junior', 'pizza']
        score = int(info[-1])  # 150

        for i in range(0, 5):
            # combinations(조합) 라이브러리 사용.
            # 예로 i가 3일 때, [(0, 1, 2), (0, 1, 3), (1, 2, 3)...] 의 모든 조합들을 만들어준다.
            case = list(combinations([0, 1, 2, 3], i))

            for c in case:
                temp = []
                for index in range(0, 4):
                    if index in c:
                        temp.append('-')  # 선택하지 않은 경우 '-'
                    else:
                        temp.append(pick[index])

                key = ''.join(temp)
                dic[key].append(score)  # key: "javabackendjuniorpizza", value: 150 를 dictionary에 append.

    return dic


def solution(info, query):
    answer = []
    dic = dataProcess(info)  # 데이터 전처리

    for value in dic.values():
        value.sort()

    for text in query:
        count = 0
        text = text.replace("and ", "")
        text = list(text.split())
        key = ''.join(text[:-1])
        value = int(text[-1])

        if dic[key]:
            index = bisect_left(dic[key], value)  # bisect_left([50, 150, 150, 150, 200], 150) => 1 을 리턴한다.
            count = len(dic[key]) - index  # 전체 길이 - index => value 이상인 원소의 갯수

        answer.append(count)

    return answer


a = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
b = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(a, b))
