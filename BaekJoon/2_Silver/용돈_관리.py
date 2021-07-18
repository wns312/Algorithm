import sys
sys.stdin = open("../input.txt", "r")

def bin_search():
    left, right = max(arr), 10000*100000
    res = 10000*100000
    while left <= right:
        middle = (left + right) // 2 # K 값
        # 여기가 수정이 들어가야 함
        cnt = 1
        remain = middle
        for i in range(N):
            remain -= arr[i]
            if remain < 0: # 잔액이 쓸 양보다 적으면?
                cnt += 1
                remain = middle
                remain -= arr[i]

        if cnt > M: # 인출 횟수가 기준보다 크면 금액 늘림
            left = middle + 1
        else: # 인출 횟수 만족 시 금액 줄임
            right = middle - 1
            if middle < res:
                res = middle
    return res

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
print(bin_search())

