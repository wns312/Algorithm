import sys
sys.stdin = open("../input.txt", "r")

def one_to_n(num):
    return num*(num+1)//2

def bin_search():
    left, right = 0, N
    res = 0
    while left <= right:
        middle = (left+right) // 2
        total = one_to_n(middle)
        if total > N:
            right = middle - 1
        else:
            left = middle + 1
            if res < middle:
                res = middle
    return res


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 징검다리 총 수
    # 반으로 나눈게 자기보다 작아야 한다
    print(bin_search())