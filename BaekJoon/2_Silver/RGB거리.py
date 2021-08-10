import sys
sys.stdin = open("../input.txt", "r")

def reculsive(idx, color_now):
    for i in range(3):
        if color_now == i: continue
        l_cost = memo[idx-1][i] # 메모된 이전 가격
        if arr[idx][color_now]+l_cost < memo[idx][color_now]:
            memo[idx][color_now] = arr[idx][color_now]+l_cost


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
memo = [list([1000000, 1000000, 1000000]) for _ in range(N)]
memo[0] = arr[0]
for i in range(1, N):
    for j in range(3):
        reculsive(i, j)
print(min(memo[-1]))
