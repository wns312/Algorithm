import sys
sys.stdin = open("../input.txt")

def bin_search():
    l, r = 1, arr[-1] # arr[0]이 아니라 1이 들어가야 하는 이유는?
    res = 1 # 집은 겹치지 않으므로 최소 1은 나온다
    while l <= r:
        m = (l + r) // 2
        cnt = 2
        min_dis = arr[-1]-arr[0]
        last_p = arr[0] # 이전에 설치한 장소 기준. 집은 0부터 시작하므로 0이 맞음
        for i in range(1, N-1):
            if arr[i]-last_p >= m and arr[-1]-arr[i] >= m:
                cnt += 1
                dis = arr[i]-last_p if arr[i]-last_p < arr[-1]-arr[i] else arr[-1]-arr[i]
                last_p = arr[i]
                if dis < min_dis:
                    min_dis = dis
        if cnt >= C: # 공유기 개수를 만족했다면 거리를 늘려본다
            l = m + 1
            if min_dis > res:
                res = min_dis
        else: # 공유기를 적게 설치했다면 거리를 줄인다.
            r = m - 1
    return res


N, C = map(int, input().split()) # 집 N개, 공유기 C개

arr = [int(input()) for _ in range(N)] # N개의 집의 좌표
arr.sort()
print(bin_search())

