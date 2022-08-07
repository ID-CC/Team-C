# 13:35 ~ 15:25 (총 110분)
import copy


def dfs(tree: [], depth, combination, visited=None):
    max_depth = len(tree)

    if depth == max_depth:
        combination.append(copy.deepcopy(visited))
        return

    if visited is None:
        visited = list()

    nodes = tree[depth]
    for node in nodes:
        if node in visited:  # 상위 level에서 대입했던 user id
            continue
        visited.append(node)
        dfs(tree, depth + 1, combination, visited)
        visited.remove(node)


def solution(user_id, banned_id):
    answer = 0

    candid_ban = [list() for _ in range(len(banned_id))]  # 각 banned_id 원소와 조건이 맞는 id를 저장하는 배열

    for idx_ban in range(0, len(banned_id)):
        for user in user_id:
            if len(user) == len(banned_id[idx_ban]):
                matched = 0
                for idx in range(0, len(user)):
                    if user[idx] == banned_id[idx_ban][idx] or banned_id[idx_ban][idx] == '*':
                        matched += 1
                if matched == len(user):
                    candid_ban[idx_ban].append(user)

    combination = list()
    dfs(candid_ban, 0, combination)
    list_concatenated = list()
    for itr in combination:
        itr.sort()
        concatenated = ''
        for itr2 in itr:
            concatenated += itr2
        list_concatenated.append(concatenated)
    list_concatenated = list(set(list_concatenated))
    answer = len(list_concatenated)

    return answer


def main():
    # user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    # banned_id = ["fr*d*", "abc1**"]
    # print(solution(user_id, banned_id))
    #
    # user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    # banned_id = ["*rodo", "*rodo", "******"]
    # print(solution(user_id, banned_id))

    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "*rodo", "******", "******"]
    print(solution(user_id, banned_id))


main()
