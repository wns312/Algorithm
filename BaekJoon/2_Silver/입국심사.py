import sys
sys.stdin = open('../input.txt', 'r')

def bin_search():
    l, r = 1, arr[0]*M
    min_time = arr[0]*M
    while l <= r:
        # 걸리는 시간. 각 심사시간을 이 시간에 가깝게 곱하고, 사람 수를 센다
        cnt = 0
        m = (l + r) // 2
        for i in range(N):
            time = arr[i] # 심사 소요 시간
            tmp = m // time # 단위 시간당 처리할 수 있는 사람 수
            if not tmp: break
            cnt += tmp
        if cnt >= M: # 기준 시간에 충분히 처리했다면 시간 갱신하고 시간 줄임
            r = m - 1
            if m < min_time:
                min_time = m
        else:
            l = m + 1
    return min_time

N, M = map(int, input().split()) # 입국 심사대 N개, 총 M명
arr = [int(input()) for _ in range(N)] # 각 심사대의 심사 소요 시간
arr.sort()
# 이진 탐색의 기준은 몇 초 이하인 심사대만 사용할 것인가?
print(bin_search())


