import sys
sys.stdin = open("../input.txt", "r")

def bin_start(idx):
    num_to_find = arr[idx]
    left, right = 0, idx
    p = idx
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == num_to_find:
            right = middle - 1
            p = middle
        else:
            left = middle + 1
    return p

def bin_search(num):
    left, right = 0, N-1
    while left <= right:
        middle = (left+right) // 2

        if arr[middle] == num:
            result = bin_start(middle)
            return result

        if arr[middle] < num:
            left = middle + 1
        else:
            right = middle - 1
    return -1


N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
nums = [int(input()) for _ in range(M)]
for i in range(M):
    print(bin_search(nums[i]))