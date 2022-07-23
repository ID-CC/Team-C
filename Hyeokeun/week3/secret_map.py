# 21:03 ~ 21:38 (25분)
def solution(n, arr1, arr2):
    answer = []

    for idx in range(0, n):
        binary = arr1[idx] | arr2[idx]
        ans = bin(binary)[2:].replace('0', ' ').replace('1', '#')
        blanks = ((2 ** n - 1) - binary)  # n = 5일 때 2 ** n - 1 = 11111, binary가 01111일 때, 10000
        itr_n = n - 1
        while blanks & 2 ** itr_n:  # 가장 상위 bit부터 bit and 연산으로 1이면 공백 추가
            ans = ' ' + ans
            itr_n -= 1
        answer.append(ans)

    return answer


def main():
    n = 6
    arr1 = [46, 33, 33, 22, 31, 50]
    arr2 = [27, 56, 19, 14, 14, 10]
    print(solution(n, arr1, arr2))


main()
