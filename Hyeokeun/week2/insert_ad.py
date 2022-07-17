from datetime import timedelta
from datetime import datetime

# 15:00 ~
class Period:
    def __init__(self, start_time: timedelta, end_time: timedelta, count=0, left=None, right=None):
        self.start_time = start_time
        self.end_time = end_time
        self.duration = int((self.end_time - self.start_time).total_seconds())
        self.left: Period = left
        self.right: Period = right
        self.count = count

    def update_duration(self):
        self.duration = int((self.end_time - self.start_time).total_seconds())

    def insert(self, log: str):
        convert_time = log.split('-')
        split_log = convert_time[0].split(':')
        log_start = timedelta(hours=int(split_log[0]), minutes=int(split_log[1]), seconds=int(split_log[2]))
        split_log = convert_time[1].split(':')
        log_end = timedelta(hours=int(split_log[0]), minutes=int(split_log[1]), seconds=int(split_log[2]))

        node_start = self
        while node_start is not None and node_start.end_time <= log_start:
            node_start = node_start.right

        distance = 0
        node_end = node_start
        while node_end is not None and node_end.end_time < log_end:
            node_end = node_end.right
            distance += 1

        # node가 head일 경우를 고려하여 node를 쪼갤 때 가장 왼쪽 구간은 새로 할당하지 않고 현재 node의 값을 변경하여 사용
        if distance == 0:
            new_nodes = list()  # 기존 node를 분할하여 새로운 구간 생성. distance가 0일 경우는 start node가 최대 3개로 분할 됨.
            node_start_end_time = node_start.end_time
            if log_start == node_start.start_time:
                node_start.end_time = log_end
                node_start.update_duration()
                node_start.count += 1
            else:
                node_start.end_time = log_start
                node_start.update_duration()
                new_nodes.append(Period(log_start, log_end, node_start.count + 1))

            if log_end != node_start_end_time:
                new_nodes.append(Period(log_end, node_start_end_time, node_start.count))

            if len(new_nodes) != 0:
                new_nodes[len(new_nodes) - 1].right = node_start.right
                node_start.right = new_nodes[0]
                left = node_start
                for idx_nodes in range(0, len(new_nodes)):
                    new_nodes[idx_nodes].left = left
                    left = new_nodes[idx_nodes]
                    if idx_nodes < len(new_nodes) - 1:
                        new_nodes[idx_nodes].right = new_nodes[idx_nodes + 1]

        else:
            # 양 끝 노드를 제외한 중간 노드들의 재생 횟수 ++
            itr_node = node_start.right
            while itr_node != node_end:
                itr_node.count += 1
                itr_node = itr_node.right

            # node start 분할
            if log_start == node_start.start_time:
                node_start.count += 1
            else:
                new_node = Period(log_start, node_start.end_time, node_start.count + 1, node_start, node_start.right)
                node_start.right = new_node
                node_start.end_time = log_start
                node_start.update_duration()

            if log_end == node_end.end_time:
                node_end.count += 1
            else:
                new_node = Period(log_end, node_end.end_time, node_end.count, node_end, node_end.right)
                node_end.right = new_node
                node_end.end_time = log_end
                node_end.update_duration()
                node_end.count += 1

    def calc_running_time(self, adv_len: timedelta, start_time: timedelta):
        end_time = start_time + adv_len
        running_time = 0

        node_start = self
        while node_start is not None and node_start.end_time <= start_time:
            node_start = node_start.right

        node_end = node_start
        while node_end is not None and node_end.end_time < end_time:
            if node_end != node_start and node_end.end_time <= end_time:
                running_time += node_end.duration * node_end.count  # start node와 end node 제외한 중간 node들의 duration은 전부 더함
            node_end = node_end.right

        running_time += (node_start.end_time - start_time).total_seconds() * node_start.count
        if node_end is not None and node_start != node_end:
            running_time += (end_time - node_end.start_time).total_seconds() * node_end.count

        return running_time, node_start

    def find_adv_time(self, adv_time: str):
        candid_start_time = list()  # 광고의 시작점이 될 수 있는 후보의 list. 로그의 시작점들과 로그의 End time - adv_len
        split_adv = adv_time.split(':')
        adv_len = timedelta(hours=int(split_adv[0]), minutes=int(split_adv[1]), seconds=int(split_adv[2]))
        itr_node = self
        while itr_node is not None:
            candid_start_time.append(itr_node.start_time)
            end_minus_adv_len = itr_node.end_time - adv_len
            if end_minus_adv_len.total_seconds() > 0:
                candid_start_time.append(end_minus_adv_len)
            itr_node = itr_node.right

        candid_start_time.sort()
        running_time_list = list()
        pos_node = self
        for itr_candid in candid_start_time:
            running_time, pos_node = pos_node.calc_running_time(adv_len, itr_candid)
            running_time_list.append(running_time)

        max_running = 0
        for idx_running_time in range(0, len(running_time_list)):
            if max_running < running_time_list[idx_running_time]:
                max_running = running_time_list[idx_running_time]
                start_time = candid_start_time[idx_running_time]

        start_time = datetime(2022, 7, 17) + start_time  # timedelta를 datatime으로 변환
        start_time = start_time.strftime('%H:%M:%S')

        return start_time


def solution(play_time, adv_time, logs):
    answer = ''

    split_play = play_time.split(':')
    start = timedelta(hours=0, minutes=0, seconds=0)
    end = timedelta(hours=int(split_play[0]), minutes=int(split_play[1]), seconds=int(split_play[2]))
    head = Period(start, end)
    for itr_logs in logs:
        head.insert(itr_logs)

    answer = head.find_adv_time(adv_time)

    return answer


def main():
    play_time = "02:03:55"
    adv_time = "00:14:15"
    logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
    answer = solution(play_time, adv_time, logs)
    print(answer)


main()
