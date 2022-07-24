def solution(n, arr1, arr2):
    answer = []

    for i in range(0, n):
        result = ""
        # bin() : OR 비트연산
        val = bin(arr1[i] | arr2[i])[2:]  # 2진수를 의미하는 "0b"를 지우기 위해 [2:] 사용. (리스트 슬라이싱)
        val = val.zfill(n)  # zfill(n) : 앞쪽 비어있는 공간을 n자리 수가 되도록 0으로 채워준다. [zfill(6) : (1010 -> 001010)]

        for item in val:
            result += '#' if item == '1' else ' '
        answer.append(result)

    return answer


if __name__ == "__main__":
    print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
    print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
