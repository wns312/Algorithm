import sys
sys.stdin = open("../input.txt")

def bin_search():
    if C == 2:
        return arr[-1] - arr[0]
    left, right = 0, arr[-1]
    res = 0
    while left <= right:
        quantity = 1
        last_length = arr[0]
        middle = (left+right) // 2
        min_dis = arr[-1] # 인접한 간격 중 제일 작은 것. 제일 큰 것으로 초기화
        for i in range(1, N): # 첫째 것과 마지막 것 제외
            house = arr[i]
            distance = arr[i] - last_length
            if distance >= middle:
                quantity += 1
                last_length = arr[i]
                if min_dis > distance:
                    min_dis = distance
                if quantity > C:
                    break
        if quantity == C:
            if min_dis > res:
                res = min_dis
            left = middle + 1
        elif quantity > C:
            left = middle + 1
        else:
            right = middle - 1
    return res

# 집 N개, 공유기 C개
N, C = map(int, input().split())
# N개의 집의 좌표
arr = [int(input()) for _ in range(N)]
arr.sort()
# 한 집에 공유기는 하나만 설치 가능하다
# 공유기 간의 거리를 최대한 크게 하고 싶다
print(bin_search())