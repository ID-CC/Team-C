from math import ceil  # math.ceil(): 반올림 함수


# 초 단위로 변환
def getSeconds(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)


def getParkingCharges(time, fees):
    # fees[0~3]
    # 기본 시간(분) / 기본 요금(원) / 단위 시간(분) / 단위 요금(원)

    if time > fees[0]:  # 기본 시간보다 오래 주차한 경우
        time = time - fees[0]  # 기본 시간 빼주기
        time = ceil(time / fees[2])  # 단위 시간으로 나누기
        time = time * fees[3]  # 주차 시간 * 요금
        return fees[1] + time  # 기본 요금 + 계산 요금
    else:
        return fees[1]  # 기본 요금 리턴


def solution(fees, records):
    answer = []

    # dictionary
    parking_lot = dict()  # key: 현재 주차되어 있는 차 번호 / value: 입차 시간
    parking_time = dict()  # key: 모든 차 번호 / value: 최종 주차 시간 기록

    for record in records:
        _time, _car, _type = record.split()
        _time = getSeconds(_time)  # 초 단위로 변환
        if _type == "IN":
            parking_lot[_car] = _time  # 입차 처리
        else:  # "OUT"인 경우
            if _car in parking_time:
                parking_time[_car] += (_time - parking_lot[_car])  # 주차 시간 계산
            else:
                parking_time[_car] = (_time - parking_lot[_car])  # 주차 시간 계산

            del parking_lot[_car]  # 출차 처리

    # 주차장에 남아있는 차 => 23:59에 출차되었다고 간주.
    for car_number in parking_lot:
        if car_number in parking_time:
            parking_time[car_number] += (1439 - parking_lot[car_number])  # 1439: "23:59"를 초 단위로 변경한 값
        else:
            parking_time[car_number] = (1439 - parking_lot[car_number])  # 1439: "23:59"를 초 단위로 변경한 값

    for car_number in sorted(parking_time):  # 오름차순 정렬
        answer.append(getParkingCharges(parking_time[car_number], fees))  # 요금 계산

    return answer


if __name__ == "__main__":
    # [14600, 34400, 5000]
    print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
    # [0, 591]
    print(solution([120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
    # [14841]
    print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
    # [8600]
    print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:34 5961 OUT", "07:34 5961 IN", "08:34 5961 OUT", "09:34 5961 IN", "10:34 5961 OUT", "11:34 5961 IN", "12:34 5961 OUT"]))
