"""테스트 1 〉	통과 (0.05ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.10ms, 10.4MB)
테스트 5 〉	통과 (0.28ms, 10.4MB)
테스트 6 〉	통과 (0.32ms, 10.4MB)
테스트 7 〉	통과 (2.16ms, 10.7MB)
테스트 8 〉	통과 (1.08ms, 10.5MB)
테스트 9 〉	통과 (0.30ms, 10.3MB)
테스트 10 〉	통과 (2.00ms, 10.2MB)
테스트 11 〉	통과 (2.89ms, 10.8MB)
테스트 12 〉	통과 (2.86ms, 10.7MB)
테스트 13 〉	통과 (0.04ms, 10.4MB)
테스트 14 〉	통과 (0.04ms, 10.3MB)
테스트 15 〉	통과 (0.03ms, 10.4MB)
테스트 16 〉	통과 (0.02ms, 10.5MB)"""

# 시간을 분 단위로 바꿔보아요
def timeToMin(time):
    [h, m] = list(map(int,time.split(':')))
    return (h * 60 + m)

# 시간과 요금표를 넣어주면 요금을 계산해줘요
def calculateFee(time, fees):
    if time <= fees[0]:
        return fees[1]
    
    div = (time - fees[0]) / fees[2]
    mod = div - int(div)
    
    if mod > 0:
        return fees[1] + (int(div)+1) * fees[3]
    else:
        return fees[1] + int(div) * fees[3]

# 풀이 시간은 40분이 걸렸어요
def solution(fees, records):
    answer = []
    
    car_dict = {}
    car_res = {}
    
    # 입력받은 record를 한번 순회해요 
    for st in records:
        # 시간, 차번호, state를 각각 변수에 담아줘요.
        # 근데 state는 안쓸거에요 ㅎ
        [time, car, state] = st.split()
        # str로 저장받은 시간을 분(int) 단위로 변환해줘요.
        time = timeToMin(time)
    
        # 입력받은 차번호가 car_dict 변수 내에 없다면 키를 하나 생성해줘요.
        if car not in car_dict.keys():
            car_dict[car] = []
            car_res[car] = 0
        
        # 해당 차번호에 입력받은 시간(분)을 push해줘요.
        car_dict[car].append(time)
        
    # car dict를 순회해요
    # 이렇게하면 i는 key값을 기준으로 순회가 가능해요.
    for i in car_dict:
        
        # 만약 리스트가 홀수라면 마지막 out이 찍히지 않았다는 뜻이에요.
        # 23:59를 분으로 입력하여 추가해줘요.
        if len(car_dict[i]) % 2 != 0:
            car_dict[i].append(timeToMin("23:59"))

        # 딕셔너리 내의 리스트를 순회해요.
        for j in range(len(car_dict[i])):
            
            # 짝수 인덱스일때에만 car_res[차량번호]에 (나간시간) - (들어온 시간) 값을 덧셈 저장해요.
            # 이렇게하면 총 누적시간을 구할 수 있어요.
            if j % 2 == 0:        
                car_res[i] += car_dict[i][j+1] - car_dict[i][j]
    
    # 마지막으로 car_res를 키값 기준으로 정렬하여 순회한 뒤
    for i in sorted(car_res):
        # 정답에 push를 해주고 각 값마다 요금을 계산해요.
        answer.append(calculateFee(car_res[i], fees))
        
    return answer