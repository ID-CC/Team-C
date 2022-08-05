# 15:28 ~ 17:12 휴식 14:00 ~ 15:14 (104 + 74 = 178분)
import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, id, x, y):
        self.parent: Node = None
        self.left: Node = None
        self.right: Node = None
        self.x: int = x
        self.y: int = y
        self.level = 0
        self.id: int = id


# 부모 노드의 X 값으로부터 좌 우로 탐색하면서 left node와 right node 탐색
# max_left, max_right는 형제 node의 자식 node를 자기의 자식 node로 잘못 구분하지 않게 하기위해 만든 경계선.
def make_tree(parent, y_list, list_node_in_x, max_left, max_right):
    for idx in range(parent.x, max_left, -1):
        if list_node_in_x[idx] is not None and list_node_in_x[idx].y == y_list[parent.level + 1]:
            parent.left = list_node_in_x[idx]
            parent.left.level = parent.level + 1
            parent.left.parent = parent
            break
    for idx in range(parent.x, max_right):
        if list_node_in_x[idx] is not None and list_node_in_x[idx].y == y_list[parent.level + 1]:
            parent.right = list_node_in_x[idx]
            parent.right.level = parent.level + 1
            parent.right.parent = parent
            break
    if parent.left is not None:
        make_tree(parent.left, y_list, list_node_in_x, max_left, parent.x)
    if parent.right is not None:
        make_tree(parent.right, y_list, list_node_in_x, parent.x, max_right)


def preorder(parent: Node, answer):
    if parent is None:
        return
    answer.append(parent.id)
    preorder(parent.left, answer)
    preorder(parent.right, answer)


def postorder(parent: Node, answer):
    if parent is None:
        return
    postorder(parent.left, answer)
    postorder(parent.right, answer)
    answer.append(parent.id)


def solution(nodeinfo):
    answer = [[]]

    # 입력 받은 node 정보를 Node class로 변환하고, 분류하여 저장
    max_x = 0
    max_y = 0
    y_list = list()  # level로 y값에 접근하기 위함
    for node in nodeinfo:
        max_x = max(node[0], max_x)
        max_y = max(node[1], max_y)
        if node[1] not in y_list:
            y_list.append(node[1])
    y_list.append(-1)  # make_tree 함수에서 if문의 조건을 늘리지 않고 out of range 방지하기 위함
    y_list.sort(reverse=True)

    list_node_in_x = [None] * (max_x + 1)  # 0번 index는 쓰이지 않을 것
    for id in range(0, len(nodeinfo)):
        node = Node(id + 1, nodeinfo[id][0], nodeinfo[id][1])
        list_node_in_x[node.x] = node
        if node.y == y_list[0]:
            root = node

    make_tree(root, y_list, list_node_in_x, -1, len(list_node_in_x))

    answer = [list(), list()]
    preorder(root, answer[0])
    postorder(root, answer[1])

    return answer


def main():
    nodeinfo = [[8, 6], [3, 5], [11, 5], [7, 4]]
    print(solution(nodeinfo))


main()
