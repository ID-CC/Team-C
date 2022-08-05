# 20:55 ~ 21:30 휴식 22:23 ~ 23:37 (총 109분)
def solution(nums):
    answer = 0

    # nums 내 3개의 숫자의 합으로 나올 수 있는 모든 경우의 수를 구함
    list_sum = list()
    for idx1 in range(0, len(nums)):
        for idx2 in range(idx1 + 1, len(nums)):
            for idx3 in range(idx2 + 1, len(nums)):
                list_sum.append(nums[idx1] + nums[idx2] + nums[idx3])

    max_num = max(list_sum)
    is_prime = [0] * (max_num + 1)  # 0번 idx 안씀. 1 ~ max_num 까지의 숫자에 대해 3개의 상태가 있음. 0 : 미확인, 1 : 소수임을 확인, 2 : 소수가 아님을 확인
    is_prime[1] = is_prime[2] = is_prime[3] = 1  # 1, 2, 3은 소수임

    flag_judge = True  # 소수가 아닌 수를 구하는 턴이면 True, 소수를 구하는 턴이면 False
    dict_last_multiply = {2: 1, 3: 1}  # key : 소수, value : 마지막으로 곱해본 수(소수가 아닌 수)
    cur = 4  # 소수인지 아닌지 판단 타겟인 수
    last_judge = 3  # 소수가 아님을 확인한 수 중 가장 큰 수

    while cur <= max_num:  # max_num 까지의 수 중 소수인 수를 구한다
        if last_judge <= cur:
            last_judge += 10
            if last_judge > len(is_prime) - 1:
                last_judge = len(is_prime) - 1
        for prime, multiple in dict_last_multiply.items():  # last_judge 이전까지의 숫자들에 대해 소수의 곱(즉, 소수가 아닌 수)인지 체크
            multiple_num = (multiple + 1) * prime
            while multiple_num <= last_judge:
                dict_last_multiply[prime] += 1
                is_prime[multiple_num] = 2
                multiple_num = (dict_last_multiply[prime] + 1) * prime
        while cur <= last_judge:  # 지금까지 소수가 아님을 확인한 수 이전의 수들은 소수이다
            if is_prime[cur] == 0:
                is_prime[cur] = 1
                dict_last_multiply[cur] = 1
            cur += 1

    for sums in list_sum:
        if is_prime[sums] == 1:
            answer += 1

    return answer


def main():
    nums = [1, 2, 7, 6, 4]
    print(solution(nums))


main()
