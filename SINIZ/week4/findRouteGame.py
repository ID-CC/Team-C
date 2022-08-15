import sys

sys.setrecursionlimit(10 ** 6)


# 재귀 횟수 제한 (default=1000) 변경

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


preorderResult = []
postorderResult = []


def preorder(node, nodeinfo):
    preorderResult.append(nodeinfo.index(node.data) + 1)
    if node.left:
        preorder(node.left, nodeinfo)
    if node.right:
        preorder(node.right, nodeinfo)


def postorder(node, nodeinfo):
    if node.left:
        postorder(node.left, nodeinfo)
    if node.right:
        postorder(node.right, nodeinfo)
    postorderResult.append(nodeinfo.index(node.data) + 1)


def solution(nodeinfo):
    # 입력 데이터를 y 데이터가 큰 순서대로 정렬
    # 불변성은 귀찮으니 무시 ㅎ
    answer = []
    sortedNode = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))

    root = None
    for node in sortedNode:
        if not root:
            root = TreeNode(node)
        else:
            current = root
            while True:
                if node[0] < current.data[0]:
                    if current.left:
                        current = current.left
                        continue
                    else:
                        current.left = TreeNode(node)
                        break
                if node[0] > current.data[0]:
                    if current.right:
                        current = current.right
                        continue
                    else:
                        current.right = TreeNode(node)
                        break
                break

    preorder(root, nodeinfo)
    postorder(root, nodeinfo)

    answer.append(preorderResult)
    answer.append(postorderResult)
    return answer
