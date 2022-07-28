import itertools, math

def getPrimeArray(n): # 에라토스테네스의 체 활용
    memo = [True for i in range(0, n)]
    memo[0] = False
    memo[1] = False
    
    for i in range(2, int(math.sqrt(n)+1)):
        if memo[i]:
            j = 2
        
        while i * j < n:
            memo[i * j] = False
            j += 1
    
    return memo

def solution(nums):
    
    answer = 0
    arr = getPrimeArray(3000)

    nCr = list(itertools.combinations(nums, 3))
    for a,b,c in nCr:
        if arr[a+b+c]:
            print(a,b,c)
            answer += 1
    
    return answer
