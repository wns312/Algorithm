import sys
sys.stdin = open("../input.txt")

def bin_search(num):
    left, right = 0, N-1
    while left <= right:
        middle = (left+right) // 2

        if arr[middle] == num:
            return 1
        elif arr[middle] < num:
            left = middle + 1
        else:
            right = middle - 1
    return 0


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
nums = list(map(int, input().split()))

for i in range(M):
    print(bin_search(nums[i]), end=" ")
