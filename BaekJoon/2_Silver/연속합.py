import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
for i in range(1, N):
    if arr[i] + arr[i - 1] > arr[i]:
        arr[i] += arr[i - 1]
print(max(arr))
