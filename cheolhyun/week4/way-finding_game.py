import sys
sys.setrecursionlimit(10 ** 6)
answer = [[], []]


def tree_order(tree, isPre):
    node = tree[0]  # 현재의 루트 노드
    left, right = [], []  # 루트 노드의 x좌표 값 기준으로 좌/우 분리

    for i in range(1, len(tree)):
        if node[0] > tree[i][0]:  # x좌표 값이 더 작으면 left
            left.append(tree[i])
        else:
            right.append(tree[i])  # 아니면 오른쪽

    # 전위 순회일 때:
    # 1. 탐색 완료한 현재 노드를 먼저 기록
    # 2. 나머지 노드에 대한 순회 진행
    if isPre:
        answer[0].append(node[2])

    # 나머지 노드에 대한 순회 진행
    if left:
        tree_order(left, isPre)
    if right:
        tree_order(right, isPre)

    # 후위 순회일 때:
    # 1. 왼쪽부터 최대한 깊게 탐색.
    # 2. 더이상 깊이 들어갈 수 없을 때의 노드 번호를 기록.
    if not isPre:
        answer[1].append(node[2])

    return


def solution(node_info):

    # 인덱스 정보 추가하기. [[5, 3], [11, 5] ..] => [[5, 3, 1], [11, 5, 2] ..]
    for i in range(len(node_info)):
        node_info[i].append(i + 1)

    # 정렬 우선순위:
    # 1순위: y좌표 순으로 내림차순 정렬. (-arr[1])
    # 2순위: x좌표 순으로 오름차순 정렬. (arr[0])
    node_info = sorted(node_info, key=lambda arr: (-arr[1], arr[0]))

    tree_order(node_info, True)  # 전위 순회
    tree_order(node_info, False)  # 후위 순회

    return answer


if __name__ == "__main__":
    print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
    # [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
