def solution(new_id):
    temp = new_id.lower()  # 1단계(소문자로 치환)
    answer = ""

    # 2단계([알파벳, 숫자, '-', '_', '.']를 제외한 모든 문자 제거.)
    for i in temp:
        if i in ['-', '_', '.'] or i.isdigit() or i.isalpha():
            answer += i

    # 3단계
    while ".." in answer:
        answer = answer.replace("..", ".")

    # answer 변수를 list 타입으로 변경함. (index를 통한 접근이 용이하도록.)
    answer = list(answer)

    # 4단계
    if answer[0] == '.' and len(answer) == 1:  # '.' 하나만 남아있을땐 clear
        answer.clear()
    elif answer[0] == '.':
        answer = answer[1:]

    if len(answer) > 1 and answer[-1] == '.':
        answer = answer[:-1]

    # 5단계 (문자열이 비어있다면 'a' 대입)
    if not answer:
        answer.append('a')

    if answer.__len__() > 15:  # 6단계
        answer = answer[:15]
    elif answer.__len__() <= 2:  # 7단계
        while answer.__len__() < 3:
            answer.append(answer[-1])

    return ''.join(answer).strip('.')  # 4단계 보완
