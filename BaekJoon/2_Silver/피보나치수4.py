import sys
sys.stdin = open('../input.txt', 'r')
# 반복으로 풀기
def dp():
    if N <= 2:
        return memo[N]
    for i in range(3, N+1):
        memo[i] = memo[i-1]+memo[i-2]


N = int(input())
memo = [0]*(N+3)
memo[1] = memo[2] = 1
dp()
print(memo[N])
