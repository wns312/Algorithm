import sys
sys.stdin = open("../input.txt", "r")
N = int(input())
arr = [int(input()) for _ in range(N)]
memo = [0, arr[0], 0]
for i in range(1, N):
    new_arr = [0, 0, 0]
    new_arr[0] = max(memo) # 0번 인덱스를 포함시키지 않으면 에러남
    new_arr[1], new_arr[2] = arr[i]+memo[0], arr[i]+memo[1]
    memo = new_arr
print(max(memo))