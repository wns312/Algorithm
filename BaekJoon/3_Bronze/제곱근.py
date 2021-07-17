# 이분탐색으로 풀어야 했다
N = int(input())
start, end = 0, N

while start <= end:
    m = (start+end)//2
    if m**2 == N:
        print(m)
        break
    if m**2 < N:
        start = m+1
    else:
        end = m-1

