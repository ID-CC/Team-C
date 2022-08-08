# 블로그를 보고 참고했읍니다. 뎨동합니다. 제 머리로는 어쩔 수 없나보아요.

def getNumberIdx(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return i


def getTailIdx(s, idx):
    for i in range(idx, len(s)):
        if not s[i].isdigit():
            return i
    return len(s)

def solution(files):
    for i in range(len(files)):
        start = getNumberIdx(files[i])
        end = getTailIdx(files[i], start)
        files[i] = (files[i][:start], files[i][start:end], files[i][end:])
    return list(map(''.join, sorted(files, key=lambda x: (x[0].lower(), int(x[1])))))

