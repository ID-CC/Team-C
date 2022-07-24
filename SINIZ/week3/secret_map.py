"""풀이 시간 5분..."""
def solution(n, arr1, arr2):
    array = []
    # 입력 배열 두개를 동시순회해요.
    for a, b in zip(arr1, arr2):
        # a와 b를 or연산 후 이진법으로 변환
        # '0b0000' 형식의 str이 리턴되는데 앞에 0b를 빼줍니당
        temp = bin(a|b)[2:]
        
        # 작은 수는 자릿수가 n만큼 안나오기에 while문을 돌려서
        # 앞에 0을 붙여서 자릿수를 n에 맞춰줍니다.
        while len(temp) < n:
            temp = '0' + temp
        
        # 나온 값에 1은 #으로, 0은 공백으로 치환하면 끝~
        temp = temp.replace('1','#').replace('0',' ')
        array.append(temp)
        
    return array