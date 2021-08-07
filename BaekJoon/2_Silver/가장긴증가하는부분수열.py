import sys
sys.stdin = open("../input.txt", "r")

def reculsive(idx):
    # 값이 있다는 것은 확정값이라는 뜻이다
    if memo[idx]:
        return memo[idx]+1
    memo[idx] = 1
    for i in range(idx):
        if arr[idx] > arr[i]:
            length = reculsive(i)
            if length > memo[idx]:
                memo[idx] = length
    return memo[idx]+1

N = int(input())
arr = list(map(int, input().split()))
memo = [0]*N
memo[0] = 1
# 길이 0이나 1일떄를 생각해보자
for i in range(N):
    reculsive(i)
print(max(memo))
