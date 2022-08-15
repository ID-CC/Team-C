# 16:50 ~ 17:21 휴식 후 재개 19:51 ~ 20:18 휴식 11:25 ~ 13:22 (31 + 27 + 57 = 115분)
# https://school.programmers.co.kr/learn/courses/30/lessons/60060
class Node:
    def __init__(self, key, data=None):
        self.key = key  # 문자열의 level 번째 문자
        self.data = data  # 해당 node까지 들어간 문자열이 존재하면 data에 None이 아닌 값
        self.children = dict()
        self.len = []
        # query 에 ?로 검색할 경우를 위한 list. Trie는 word로 만들어지고 search 함수의 input에 query가 들어가는데, node를 타고 들어가다가 '?'를
        # 만나면 len list에서 query 문자열 길이와 같은 길이를 갖는 list내 원소의 개수를 세어서 답 도출


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        len_word = len(string)
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node.len.append(len_word)
            curr_node = curr_node.children[char]
        curr_node.data = string

    def search(self, string):
        len_word = len(string)
        curr_node = self.head
        for char in string:
            if char == '?':
                return curr_node.len.count(len_word)
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return 0

# 처음 풀이시에 query의 ?를 제외한 문자열의 시작점과 끝점을 binary search로 찾고, word와 query 문자열을 slicing하여 동일 비교하였는데, 효율성 4, 5만 통과
# 이후 질문하기에서 Trie 구조에 대한 글을 보고 새로 짬
# def find_start_end_idx(query):
#     word_start, word_end = 0, len(query)
#     start, end = 0, len(query) - 2  # 연속 된 두 문자열을 비교하기 위한 것이므로 mid 값은 len - 1보다 한 칸 더 앞이어야 함
#     if query[0] == '?':  # query가 ?로 시작하면
#         while start <= end:
#             mid = (start + end) // 2
#             if query[mid] == '?' and query[mid + 1] != '?':  # target hit
#                 word_start = mid + 1
#                 break
#             elif query[mid] == '?':  # ?가 앞에 있으므로 더 뒤쪽을 찾아야 함
#                 start = mid + 1
#             else:
#                 end = mid - 1
#     else:  # query가 문자열로 시작하면
#         while start <= end:
#             mid = (start + end) // 2
#             if query[mid] != '?' and query[mid + 1] == '?':  # target hit
#                 word_end = mid + 1  # slice 할 땐 end는 한 칸 더 가야함
#                 break
#             elif query[mid] == '?':  # ?가 뒤에 있으므로 더 앞쪽을 찾아야 함
#                 end = mid - 1
#             else:
#                 start = mid + 1
#
#     return [word_start, word_end]


def solution(words, queries):
    answer = []

    trie = Trie()
    trie_reverse = Trie()
    for word in words:
        trie.insert(word)
        trie_reverse.insert(word[::-1])

    for query in queries:
        if query[0] == '?':
            answer.append(trie_reverse.search(query[::-1]))
        else:
            answer.append(trie.search(query))

    return answer


def main():
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    print(solution(words, queries))


main()
