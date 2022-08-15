from itertools import permutations


def check_id(perm, banned_id):
    count = 0

    for idx, ban in enumerate(banned_id):
        if len(ban) != len(perm[idx]):  # 길이가 다르다면 고려 대상이 아님.
            continue

        temp = list(perm[idx])
        isPotential = True

        for i in range(len(ban)):
            if ban[i] == '*':  # 같은 index 값을 '*'로 만들면서 비교한다.
                temp[i] = '*'

            if ban[i] != temp[i]:
                isPotential = False
                break

        if isPotential:
            count += 1

    return count


def solution(user_id, banned_id):
    result = []

    # permutations: 순열을 만들어서 반환해주는 모듈.
    # permutations([A, B, C], 2) => (A, B), (A, C), (B, C), (B, A), (C, A), (C, B)
    _permutation = list(permutations(user_id, len(banned_id)))

    # 해당 조합(순열)과 banned_id의 구성을 비교하여, 가능성이 있는 조합을 result에 append 시켜준다.
    for temp in _permutation:
        count = check_id(temp, banned_id)  # 가능성이 있는 원소의 개수를 반환한다.

        user = set(temp)  # 중복 제거를 위해 set으로 전환

        # "banned_id 의 원소의 개수"와 "가능성이 있는 원소의 개수"가 같다면 +1
        if count == len(banned_id) and user not in result:
            result.append(user)

    return len(result)


if __name__ == "__main__":
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))  # 2
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))  # 2
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))  # 3
