"""
- 입력받는 모든 시간들을 "초" 단위로 변환하여 저장시킨다.
- 리스트 arr[]의 index와 시간(초)를 매칭하여, 누적 시청자 수를 기록한다.
    - 32비트 파이썬에서는 536,870,911개,
    - 64비트 파이썬에서는 1,152,921,504,606,846,975개까지 리스트의 크기를 지정할 수 있다.
    - play_time의 입력 범위: 00:00:01 ~ 99:59:59
        - 99:59:59를 초 단위로 환산하면 360000-1 이 된다.
    - 따라서, 최대 arr[360000] 크기의 리스트를 충분히 선언하여 활용할 수 있다.

- arr[]에 기록되어 있는 누적 시청자 수를 기반으로 "구간합"을 구한다.
    - 구간 : 임의의 시작 지점 ~ 광고 재생 시간
- 구간합을 구할 수 있는 경우의 수 중 최대값을 찾아내어, 해당 구간의 "임의의 시작 지점"을 리턴한다.
"""


# 영상 길이, 광고 길이, 시청 기록(list)
def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"

    play_time_sec = time_to_sec(play_time)
    adv_time_sec = time_to_sec(adv_time)

    arr = [0] * (play_time_sec + 1)  # index 맞추려고 +1

    for log in logs:
        start_time, end_time = log.split("-")
        start_time = time_to_sec(start_time)
        end_time = time_to_sec(end_time)
        arr[start_time] += 1
        arr[end_time] -= 1

    # arr[]에 해당 시간(초)의 누적 시청자 수를 기록한다.
    # e.g.) 2명의 시청자가 각각 300초 ~ 600초, 400초 ~ 600초 구간을 시청한 경우
    # arr[310] = 1 / arr[450] = 2 / arr[601] = 0
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]

    _max = 0  # 구간합의 최대값을 저장
    _time = 0  # 구간합이 최대 지점이 되는 시간(광고 시작 시간)을 저장
    prefix = 0  # 구간합 계산

    for i in range(1, len(arr) - adv_time_sec):
        # 현재 지점(i) 부터 광고 재생 시간(adv_time_sec) 까지의 누적 시청자 수를 계산.
        prefix = prefix - arr[i - 1] + arr[i + adv_time_sec - 1]  # 재생 시간은 이상/미만으로 계산해야 한다.

        # 누적 시청자 수가 이전(i-1)보다 많다면, 광고 시작 시간을 갱신한다.
        if prefix > _max:
            _time = i
            _max = prefix

    return seconds_to_time(_time)


def time_to_sec(time):
    h, m, s = time.split(':')
    seconds = int(h) * 3600
    seconds += int(m) * 60
    seconds += int(s)
    return seconds


def seconds_to_time(seconds):
    h = seconds // 3600
    h = '0' + str(h) if h < 10 else str(h)
    seconds = seconds % 3600
    m = seconds // 60
    m = '0' + str(m) if m < 10 else str(m)
    seconds = seconds % 60
    s = '0' + str(seconds) if seconds < 10 else str(seconds)
    return h + ':' + m + ':' + s


if __name__ == "__main__":
    print(solution("02:03:55", "00:14:15",
                   ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30",
                    "01:30:59-01:53:29"]))
    print(solution("99:59:59", "25:00:00",
                   ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
    print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
