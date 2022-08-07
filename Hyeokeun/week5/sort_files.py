# 11:29 ~ 12:22 휴식 12:37 ~ 13:33 (53 + 56 = 109분)
def pars_file_name(file: str) -> []:
    pos1 = 0
    pos2 = 0

    output = []

    process = 0  # 0 : head, 1 : number, 2 : tail
    for idx in range(0, len(file)):
        char = str(file[idx])

        if char.isdigit():
            if process == 0:
                process = 1
                if pos2 == 0:  # 파일 이름이 숫자로 시작
                    output.append('')
                else:
                    output.append(file[pos1:pos2])
                pos1 = idx
        else:
            if process == 1:
                process = 2
                output.append(file[pos1:pos2])
                pos1 = idx
                break
        pos2 += 1

    output.append(file[pos1:len(file)])

    if process < 2:
        output.extend([''] * (2 - process))

    return output


def solution(files):
    answer = []

    pars_files = list()  # head, number, tail 순으로 저장 되어있는 배열

    for file in files:
        parsed = pars_file_name(file)
        pars_files.append(parsed)

    pars_files.sort(key=lambda x: (str(x[0]).lower(), int(x[1])))

    for parsed in pars_files:
        answer.append(parsed[0] + parsed[1] + parsed[2])

    return answer


def main():
    files = [" 123 ", "abc132", "123abd", "dfjka 3411 .dd2"]
    print(solution(files))

    files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    print(solution(files))

    files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
    print(solution(files))


main()
