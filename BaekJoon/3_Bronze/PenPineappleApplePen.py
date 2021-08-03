import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
arr = list(input())
cnt = 0
i = 0
next_p = 0
while i < N-3:
    if arr[i] == 'p':
        if arr[i]+arr[i+1]+arr[i+2]+arr[i+3] == 'pPAp':
            cnt += 1
            i += 3
    i += 1
print(cnt)
