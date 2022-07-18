from typing import Dict


# 13:06 ~ 14:08 (62분)
def solution(id_list, report, k):
    answer = [''] * len(id_list)

    mail_cnt_dict: Dict[str, int] = dict()  # mail_cnt_dict[str(name_reporter)] = mail_cnt
    for itr_id_list in id_list:
        mail_cnt_dict[itr_id_list] = 0

    rpt_split = [''] * len(report)
    for idx_report in range(0, len(report)):
        rpt_split[idx_report] = report[idx_report].split(' ')  # rpt_split[idx_report] = [name_reporter, name_reported]

    history_report: Dict[str, Dict[str, int]] = dict()  # {reported: List[reporter]}
    for itr_rpt in rpt_split:
        reporter = itr_rpt[0]
        reported = itr_rpt[1]
        if history_report.get(reported) is None:
            history_report[reported] = dict()
        if history_report[reported].get(reporter) is None:
            history_report[reported][reporter] = 0
        else:
            history_report[reported][reporter] += 1

    for reported, reporter_dict in history_report.items():
        if len(reporter_dict) >= k:
            for reporter in reporter_dict.keys():
                mail_cnt_dict[reporter] += 1

    for idx_ans in range(0, len(answer)):
        answer[idx_ans] = mail_cnt_dict[id_list[idx_ans]]

    return answer


def main():
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
    k = 2
    answer = solution(id_list, report, k)
    print(answer)


main()
