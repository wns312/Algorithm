import sys
sys.stdin = open('../input.txt', 'r')
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for r in range(N-2, -1, -1): # 세로
    for c in range(len(arr[r])): # 가로
        arr[r][c] += max(arr[r+1][c], arr[r+1][c+1])

print(arr[0][0])