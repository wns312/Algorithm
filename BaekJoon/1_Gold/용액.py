import sys
sys.stdin = open("../input.txt", "r")

def get_a(a, b_value):
    left, right = 0, a
    res_a = a
    while left <= right:
        middle = (left + right) // 2
        new_mix = arr[middle] + b_value
        # new_mix가 mixed보다 무조건 작다 mixed는 무조건 양수
        if new_mix == 0:
            return middle
        elif new_mix > 0:
            right = middle - 1

        else:
            left = middle + 1
        a = middle  # a 위치 갱신
    return a


def get_min_dif(a, b):
    mixed = arr[a] + arr[b]
    res_a, res_b = a, b
    while mixed != 0 and a > 0 and b < N:
        if mixed == 0:
            return a, b # 혼합액이 0이면 더이상 구하지 않고 리턴
        elif mixed > 0: # 혼합액이 양수면 a가 이동
            get_a(a, arr[b])
        else: # 혼합액이 음수면 b가 이동
            pass


def get_middle():
    left, right = 0, N-1 # left가 0에가까운 양수, right가 음수
    while left <= right:
        middle = (left+right)//2
        if arr[middle] >= 0: # 0보다 크다면 b 갱신
            right = middle - 1
        else: # 0보다 작다면 a 갱신
            left = middle + 1
    get_min_dif(right, left)

N = int(input()) # 전체 용액의 수
arr = list(map(int, input().split())) # 용액의 특성값

# 두 용액을 섞어 가장 특성값이 0에 가까운 용액을 만드시오
print(arr)
# get_middle()
print(get_a(5, 98))



