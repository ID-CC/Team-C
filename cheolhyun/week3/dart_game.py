def solution(dartResult):
    values = []  # 숫자 저장용
    operators = []  # 연산자 저장용
    idx = 0
    count = 0

    for i in range(0, len(dartResult)):
        if dartResult[i].isdigit():  # 숫자 여부
            if dartResult[i] == '0' and i > 0 and dartResult[i-1].isdigit():  # '1','0' 을 10 으로.
                values[-1] = 10
            else:
                values.append(int(dartResult[i]))
        else:
            operators.append(dartResult[i])  # 연산자

    while len(operators) > idx:
        if operators[idx] in ['S', 'D', 'T']:
            if operators[idx] == 'D':
                values[count] = (values[count] * values[count])  # 제곱
            elif operators[idx] == 'T':
                values[count] = (values[count] * values[count] * values[count])  # 세제곱

            count += 1
            idx += 1
        else:  # '*' 또는 '#'
            if operators[idx] == '*':  # 해당 점수를 2배로.
                values[count-1] = values[count-1] * 2
                if idx > 1:  # 바로 전에 얻은 점수도 2배로.
                    values[count-2] = values[count-2] * 2
            elif operators[idx] == '#':  # 해당 점수를 마이너스 처리.
                values[count-1] = values[count-1] * (-1)

            idx += 1

    return sum(values)


if __name__ == "__main__":
    print(solution("1S2D*3T"))  # 37
    print(solution("1D2S#10S"))  # 9
