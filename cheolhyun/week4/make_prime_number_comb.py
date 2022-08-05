from itertools import combinations


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    # combination : nums 배열에 들어있는 모든 원소 중, 3자리 조합으로 가능한 모든 경우의 수를 만들어준다.
    comb = list(combinations(nums, 3))

    for temp in comb:  # temp => (1, 2, 3), (1, 2, 4), (1, 3, 4)... 
        if is_prime(sum(temp)):
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 4]))  # 1
    print(solution([1, 2, 7, 6, 4]))  # 4
