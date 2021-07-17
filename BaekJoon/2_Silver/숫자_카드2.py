import sys
sys.stdin = open("../input.txt")

def find_quantity(idx):
    # 시간초과이므로 이것도 이진탐색으로 찾아낸다?
    num_to_find = arr[idx]
    start, end = 0, N-1 # 초기화. 이 숫자의 시작과 끝
    # 숫자의 시작 찾기
    left, right = 0, idx
    while left <= right:
        middle = (left+right) // 2

        if arr[middle] == num_to_find:
            right = middle - 1
            start = middle
        else : # 작은 수라면
            left = middle + 1
    # 숫자의 끝 찾기
    left, right = idx, N-1
    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == num_to_find:
            left = middle + 1
            end = middle
        else:  # 큰 수라면
            right = middle - 1
    return end-start+1

def bin_search(num):
    left, right = 0, N-1
    while left <= right:
        middle = (left+right) // 2

        if arr[middle] == num:
            res = find_quantity(middle)
            # 개수 확인 로직 시작
            return res
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
