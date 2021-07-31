import sys
sys.stdin = open("../input.txt", "r")

# min_dif를 구해서 그 값에 맞는 인덱스를 리턴해주어야 함
def get_a(a, b_value):
    left, right = 0, a
    min_dif = abs(b_value + arr[a])
    while left <= right:
        middle = (left + right) // 2
        new_dif = abs(b_value+arr[middle])
        if new_dif <= min_dif: # 차이가 더 적다면
            min_dif = new_dif
            right = middle - 1
            a = middle
            if new_dif == 0:
                return middle
        else:
            left = middle + 1
    return a

def get_b(a_value, b):
    left, right = b+1, N-1
    min_dif = abs(a_value+arr[b])
    while left <= right:
        middle = (left + right) // 2
        new_dif = abs(a_value+arr[middle])
        if new_dif <= min_dif: # 차이가 더 적다면
            min_dif = new_dif
            left = middle +1
            b = middle
            if new_dif == 0:
                return middle
        else:
            right = middle - 1
    return b


def get_mixed(a, b):
    mixed = arr[a] + arr[b] # 혼합 용액
    res_a, res_b = a, b
    while mixed: # mixed가 0이 아닌 동안 돌림
        if mixed > 0 and a != 0:
            a = get_a(a-1, arr[b])
            if abs(arr[a]+arr[b]) < abs(mixed):
                res_a, res_b = a, b

        else:
            b = get_b(arr[a], b+1)
            if abs(arr[a]+arr[b]) < abs(mixed):
                res_a, res_b = a, b
        mixed = arr[a] + arr[b]

        if a <= 0 and b >= N-1:
            break
    return res_a, res_b

# 절대값이 작은애를 리턴해야 한다.
def get_middle():
    left, right = 0, N-1 # left가 0에가까운 양수, right가 음수
    middle = (left + right) // 2
    while left <= right:
        if arr[middle] >= 0: # 0보다 크다면 b 갱신
            right = middle - 1
        else: # 0보다 작다면 a 갱신
            left = middle + 1
        middle = (left + right) // 2
    if middle == 0:
        return 0, 1
    return (middle-1, middle) if abs(arr[middle-1]+arr[middle]) < abs(arr[middle]+arr[middle+1]) else (middle, middle+1)


N = int(input()) # 전체 용액의 수
arr = list(map(int, input().split())) # 용액의 특성값
# print(arr)
# 두 용액을 섞어 가장 특성값이 0에 가까운 용액을 만드시오

a, b = get_middle()
# print(a, b)
a, b = get_mixed(a, b)
print(arr[a], arr[b])

# print(get_a(3, 50))
# print(get_b(-99, 1))



