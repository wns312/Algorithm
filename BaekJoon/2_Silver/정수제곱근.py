# 0 처리해주는 것이 문제였다
N = int(input())
start, end = 0, N//2
m = (start+end)//2
while start <= end:

    if m**2 == N:
        break
    if m**2 < N:
        start = m+1
    else:
        end = m-1
    m = (start + end) // 2
if N == 0:
    print(m)
else:
    print(m+1)