# 13:31 ~ 14:38 (67분)
def solution(dartResult):
    answer = 0

    scores = []
    prizes = []
    pos1 = 0
    pos2 = 0
    b_finding_score = True
    for char in range(0, len(dartResult)):
        if b_finding_score and not ord('0') <= ord(dartResult[char]) <= ord('9'):
            b_finding_score = False
            if dartResult[char] == 'D':
                scores.append(int(dartResult[pos1:pos2]) ** 2)
            elif dartResult[char] == 'T':
                scores.append(int(dartResult[pos1:pos2]) ** 3)
            else:
                scores.append(int(dartResult[pos1:pos2]))
            if char + 1 < len(dartResult):
                if dartResult[char + 1] == '*' or dartResult[char + 1] == '#':
                    prizes.append(dartResult[char + 1])
                else:
                    prizes.append('')
            else:
                prizes.append('')
        elif not b_finding_score and ord('0') <= ord(dartResult[char]) <= ord('9'):
            b_finding_score = True
            pos1 = char
        pos2 += 1

    for idx in range(0, len(scores)):
        score = int(scores[idx])
        prize = prizes[idx]
        if prize == '#':
            scores[idx] = str(-score)
            answer += -score
        elif prize == '*':
            if idx > 0:
                answer += int(scores[idx - 1])
            scores[idx] = int(score * 2)
            answer += score * 2
        else:
            answer += score

    return answer


def main():
    dartResult = '1S*2T*3S'
    print(solution(dartResult))


main()
