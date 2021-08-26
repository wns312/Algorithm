import sys
sys.stdin = open("../input.txt", "r")
N = int(input())
memo = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# 여기에서 계산하면 된다
for i in range(1, N):
    arr = [0]*10
    arr[0], arr[9] = memo[1], memo[8]
    for j in range(1, 9):
        arr[j] = memo[j-1]+memo[j+1]
    memo=arr
print(sum(memo) % 1000000000)