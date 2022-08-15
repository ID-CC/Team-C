import sys
sys.setrecursionlimit(100001)


def solution(words, queries):
    answer = []

    rev_words = []  # words 원소들을 전부 뒤집어서 저장
    words_length = []  # words 원소들의 길이 저장
    for word in words:
        rev_words.append(word[::-1])  # reversed 처리
        words_length.append(len(word))

    trie = make_trie(words)  # 정방향 trie
    rev_trie = make_trie(rev_words)  # 역방향 trie

    for query in queries:
        if query[0] == '?' and query[-1] == '?':  # 모든 글자가 '?'인 경우
            answer.append(words_length.count(len(query)))
        elif query[0] == '?':  # '?'로 시작하는 경우 (reversed trie)
            answer.append(search_trie(rev_trie, query[::-1], len(query)))
        elif query[-1] == '?':  # '?'로 끝나는 경우 (forward trie)
            answer.append(search_trie(trie, query, len(query)))

    return answer


# 주어진 문자열로 trie 구조를 만들어서 반환함.
def make_trie(words):
    trie = dict()
    for word in words:
        cur = trie
        for w in word:
            if w in cur:
                cur = cur[w]
                cur['!'].append(len(word))  # '!'를 key로 하여 문자열의 길이 저장
            else:
                cur[w] = {}
                cur = cur[w]
                cur['!'] = [len(word)]
    return trie


# '?'가 나올 때까지 재귀로 탐색
#   - '?'를 찾았을 때, 문자열의 길이가 같은 word의 개수만큼 반환.
def search_trie(trie, query, length):
    count = 0
    if query[0] == '?':
        return trie['!'].count(length)
    elif query[0] in trie:
        count += search_trie(trie[query[0]], query[1:], length)  # 재귀

    return count


if __name__ == "__main__":
    # [3, 2, 4, 1, 0]
    print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
