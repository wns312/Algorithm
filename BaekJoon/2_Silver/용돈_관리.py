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
# 인출 최소 금액을 구하는 문제
# 1. 인출했는데 사용할 수 있으면 그대로 사용한다. 남은 건 다음날 사용
# 2. 부족하면 K만큼의 차액을 다시 넣고 K원을 인출
# 3. M번을 꼭 다 사용할 필요는 없다
# K가 최소이기만 하면 된다
arr = [int(input()) for _ in range(N)]
print(bin_search())




# 500