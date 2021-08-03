import sys
sys.stdin = open('../input.txt', 'r')

def reculsive(l, nr, nc):
    if l == 1:
        return arr[nr][nc]

    num = arr[nr][nc]
    for r in range(nr, nr+l):
        for c in range(nc, nc+l):
            if arr[r][c] != num: # 전체가 똑같지 않으면 9번 호출해야 한다
                break


N = int(input())
arr = [list(input().split()) for _ in range(N)]

for i in range(N):
    print(arr[i])