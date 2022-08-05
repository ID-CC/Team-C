def solution(files):
    answer = []

    for name in files:
        for i in range(len(name)):
            head, number, tail = '', '', ''

            if name[i].isdigit():  # 숫자 판별
                head = name[:i]
                number = name[i:]  # head/number 분리 (인덱스 슬라이싱)

                for x in range(len(number)):  # number를 기준으로 다시 한번 더 분리 작업
                    if not number[x].isdigit():
                        tail = number[x:]
                        number = number[:x]
                        break
                answer.append([head, number, tail])  # 2차원 배열 형태로 head,number,tail을 보관
                break

    # 1순위: head, 2순위: number 기준 오름차순 정렬
    answer = sorted(answer, key=lambda arr: (str(arr[0]).upper(), int(arr[1])))

    result = []
    for arr in answer:  # 다시 1차원 배열로 전환하기
        result.append(''.join(arr))

    return result
    # 아래처럼 쓰면 한 줄로도 해결 가능함.
    # return [''.join(x) for x in answer]


if __name__ == "__main__":
    print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
    print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
