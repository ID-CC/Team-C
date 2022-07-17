# 문자열 8자리 형식으로 받은 팡고 시간을 초 단위로 변환한다.
def timeToInt(string):
    time = string.split(":")
    start_time = list(map(int, time))
    time_integer = start_time[0] * 3600 + start_time[1] * 60 + start_time[2]
    return time_integer


# 숫자 (초) 형식으로 받은 시간을 문자열 8자리 HH:mm:ss 단위로 변환한다.
def intToTime(time):
    h = time // 3600
    m = (time % 3600) // 60
    s = (time % 3600) % 60

    if h < 10:
        h = "0" + str(h)
    if m < 10:
        m = "0" + str(m)
    if s < 10:
        s = "0" + str(s)
    return f"{h}:{m}:{s}"


# 푼 시간 : 회사에서 풀었음, 업무 포함 풀이 시간 자체는 5시간 ( 실 풀이 시간 2시간 30분 )
def solution(play_time, adv_time, logs):
    # 영상 재생시간, 팡고시간을 숫자형식으로 변환한다.
    ad = timeToInt(adv_time)
    # +1을 준 이유는 안주면 추후 Index범위를 초과할 수 있기 때문. 
    pt = timeToInt(play_time)+1

    # (무지성) 전체 영상 길이만큼의 배열 생성
    array = [0 for i in range(pt)]

    # 입력 데이터 로그 숫자로 변환하여 영상길이 배열에 해당 인덱스로 접근하여 현재 값에다가 1을 더함
    # 즉, 특정 시점에 현재 사용자의 수를 찍어낼 수 있음
    for i in logs:
        [start, end] = i.split("-")
        [start, end] = [timeToInt(start), timeToInt(end)]
        array[start] += 1
        array[end] -= 1

    # 현재 인덱스에 직전인덱스의 값을 더해서 넣음.
    # 이렇게하면 특정 구간에 총 사용자가 몇 중첩으로 있는지 알 수 있음.
    for i in range(1, len(array)):
        array[i] += array[i - 1]

    # 근데 그렇게 안할거임 ㅋㅋㄹㅃㅃ
    # 현재 인덱스에 직전인덱스의 값을 더해서 넣음.
    # 이렇게 하면 각 구간에 대해 누적된 조회 수를 구할 수 있음
    for i in range(1, len(array)):
        array[i] += array[i - 1]

    # 우리는 영상길이 내에서 누적된 조회수가 최대가 되는 구간을 찾아야 하므로
    # 최대값의 초기값은 0번 인덱스부터 광고시간 끝날때 까지의 조회 수
    # 조회수는 (영상 끝나는시간) - (영상 시작 시간) 으로 구한다.
    max_val = array[ad - 1]
    idx = 0

    # 광고가 끝나는 곳으로 부터 영상 재생길이까지 FOR 문
    # 만약 반복문 내에서 돌아가는 조회수 검사 값이 최대값보다 크면
    # 최대값에 탐색한 최대값을 저장한다.
    # 인덱스 값에 현재 (i - 광고시간)에다가 1을 더해 저장한다 (안그러면 -1된 값이 저장됨.)
    # ex. 01:00:00 -> 00:59:59
    for i in range(ad - 1, pt):
        if max_val < array[i] - array[i - ad]:
            max_val = array[i] - array[i - ad]
            idx = i - ad + 1

    return intToTime(idx)
