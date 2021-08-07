import sys
sys.stdin = open('../input.txt', 'r')

def dp(day = 0, total = 0):
    if day >= N: return
    ti, pi = arr[day] # Ti: 걸리는 일 수 & Pi: 받을 수 있는 금액
    dp(day+1, total) # 패스하는 경우
    if pi+total > memo[day] and day+ti <= N:
        memo[day] = total+pi
        dp(day+ti, total+pi)


N = int(input())
memo = [0]*N
arr = [list(map(int, input().split())) for i in range(N)]
dp()
print(max(memo))