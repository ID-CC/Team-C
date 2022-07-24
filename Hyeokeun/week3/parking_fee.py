# 16:58 ~ 17:48 (휴식) 19:09 ~ 19:20 (61분)
# 입력은 요금표와 입출문 기록
# 입차 기록 후 출차 기록이 없다면 23:59에 출차 된 것으로 간주
# 누적 주차 시간이 기본 시간 이하라면 기본 요금을 청구
# 요금 = 기본 요금 + ceiling((이용 시간 - 기본 시간) / 단위 시간) * 단위 요금
# 차량 번호가 작은 자동차부터 청구할 주차 요금을 정수 배열에 담아 return
import math


def time_to_int(time: str):
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)


def int_to_time(input_time: int):
    hour = input_time // 60
    minute = input_time % 60
    return str(hour) + ':' + str(minute)


def solution(fees, records):
    answer = []

    base_time = fees[0]
    base_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    # records의 각 원소는 "시각 차량번호 내역"
    records_dict = dict()  # 차량 번호를 key로 갖고 시간과 내역을 list로 잠시 갖고있는 dictionary
    accum_time = dict() # 차량 번호를 key로 갖고 누적 주차장 이용시간을 값으로 갖는 dictionary
    for record in records:
        time, number, in_out = record.split(' ')
        if records_dict.get(number) is None:  # 지금 나온 data가 입문 기록임
            records_dict[number] = time
        else:  # 지금 나온 data가 출문 기록임
            if accum_time.get(number) is None:
                accum_time[number] = 0
            accum_time[number] += time_to_int(time) - time_to_int(records_dict[number])
            del records_dict[number]
    # 출문 기록이 없는 차량에 대한 추가 작업
    for number in records_dict.keys():  # 출문 기록에 대한 작업 시 data를 지웠기 때문에 해당 for문은 입문 기록이 마지막인 차량들에 대해서만 수행될 것
        if accum_time.get(number) is None:
            accum_time[number] = 0
        accum_time[number] += time_to_int('23:59') - time_to_int(records_dict[number])

    # 요금 계산
    fee_cars = dict()
    for number in accum_time.keys():
        parking_time = accum_time[number]
        if parking_time <= base_time:
            fee_cars[number] = base_fee
        else:
            fee_cars[number] = base_fee + math.ceil((parking_time - base_time)/unit_time) * unit_fee

    sorted_fee = sorted(fee_cars.items())
    for number, fee in sorted_fee:
        answer.append(fee)

    return answer


def main():
    fees = [1, 461, 1, 10]
    records = ["00:00 1234 IN"]
    print(solution(fees, records))


main()
