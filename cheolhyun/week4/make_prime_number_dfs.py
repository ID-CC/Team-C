"""
- dfs로 구현함.
  - 입력받은 nums 중 모든 3자리수 조합을 점검
  - 소수로 판별되면 count += 1
"""

arr = []  # dfs로 탐색하면서 숫자를 저장시켜놓는다.
count = 0


def dfs(_nums, idx, _len):
    global count

    if _len == 3:  # arr에 원소가 3개일 때
        if is_prime(sum(arr)):
            count += 1
        return

    for i in range(idx, len(_nums)):
        if _len < 3:
            arr.append(_nums[i])  # 현재 숫자를 arr에 넣어준다
            dfs(_nums, i+1, _len+1)
            arr.pop()  # 맨 오른쪽 숫자를 제거해주면서, 모든 경우의 수를 탐색할 수 있게 된다.


# 소수 판별 함수
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(nums):
    global count
    count = 0

    dfs(nums, 0, 0)
    return count


if __name__ == "__main__":
    print(solution([1, 2, 3, 4]))  # 1
    print(solution([1, 2, 7, 6, 4]))  # 4
