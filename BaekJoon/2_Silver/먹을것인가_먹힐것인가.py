import sys
sys.stdin = open("../input.txt", "r")

def bin_search(num):
    left, right = 0, B-1
    idx = -1
    while left <= right:
        middle = (left + right) // 2

        if arr[middle] < num: # 잡아먹을 수 있다면
            left = middle + 1
            idx = middle
        else:
            right = middle - 1
    return idx+1

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    to_find = list(map(int, input().split())) # 하나씩 꺼내서 arr에서 찾는다.
    arr = list(map(int, input().split()))
    arr.sort()
    result = 0
    for i in range(A):
        result += bin_search(to_find[i])
    print(result)

# 7
# 1