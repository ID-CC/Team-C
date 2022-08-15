def isMatch(query, word):
    for i in range(0, len(word)):
        if query[i] == '?':
            continue
        if word[i] != query[i]:
            return False

    return True


def solution(words, queries):
    answer = []

    for index, query in enumerate(queries):
        answer.append(0)
        for word in words:
            if len(query) != len(word):
                continue

            if isMatch(query, word):
                answer[index] += 1

    return answer


if __name__ == "__main__":
    # [3, 2, 4, 1, 0]
    print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))

# 시간복잡도: O(N^3) (3중 for문으로 구현)
# 정확성 테스트 통과
# 효율성 테스트 2/5 통과


"""
정확성
테스트 1 〉	통과 (0.34ms, 10.2MB)
테스트 2 〉	통과 (0.21ms, 10.2MB)
테스트 3 〉	통과 (0.25ms, 10.2MB)
테스트 4 〉	통과 (0.18ms, 10.2MB)
테스트 5 〉	통과 (0.24ms, 10.2MB)
테스트 6 〉	통과 (0.21ms, 10.1MB)
테스트 7 〉	통과 (10.73ms, 10.3MB)
테스트 8 〉	통과 (12.88ms, 10.2MB)
테스트 9 〉	통과 (17.60ms, 10.4MB)
테스트 10 〉	통과 (9.97ms, 10.3MB)
테스트 11 〉	통과 (8.58ms, 10.2MB)
테스트 12 〉	통과 (10.72ms, 10.4MB)
테스트 13 〉	통과 (208.39ms, 10.3MB)
테스트 14 〉	통과 (180.40ms, 10.6MB)
테스트 15 〉	통과 (181.00ms, 10.5MB)
테스트 16 〉	통과 (212.06ms, 10.3MB)
테스트 17 〉	통과 (188.06ms, 10.5MB)
테스트 18 〉	통과 (196.14ms, 10.4MB)

효율성
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	통과 (632.40ms, 13.3MB)
테스트 5 〉	통과 (618.14ms, 13.6MB)
"""