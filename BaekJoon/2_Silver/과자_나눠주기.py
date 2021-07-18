import sys
sys.stdin = open("../input.txt", "r")

# 여기 수정 필요. 가장 작은 과자보다 작은 길이로 분배하는 경우 고려
def bin_start(num):
    left, right = 0, N-1
    idx = N-1
    while left <= right:
        middle = (left + right) // 2 # 인덱스 시작점
        # num의 시작점을 찾는다
        if arr[middle] >= num: # 만약 숫자가 같거나 크다면?
            right = middle - 1
            idx = middle
        else:
            left = middle + 1
    return idx

def bin_search():
    left, right = 1, arr[-1] # 과자 길이가 정렬된 상태임을 가정함
    length = 0
    while left <= right:
        middle = (left + right) // 2 # 막대 과자의 길이
        start = bin_start(middle)
        # 과자 하나로 여러 조카를 먹일 수 있다.
        quantity = sum(arr[i] // middle for i in range(start, N))
        # 만들 수 있는 과자 개수
        # print(f"과자의 길이가 {middle}일 때, 나누어 줄 수 있는 과자 개수 {quantity}")
        if quantity < M: # 나눠줄 수 있는 과자의 수가 조카보다 작다면? 사이즈 줄여야지
            right = middle - 1
        else: # 나눠줄 수 있는 과자의 수가 조카의 수와 같거나 크다면? 사이즈 키워야지
            left = middle + 1
            if length < middle:
                length = middle
    return length


# 조카의 수 M, 과자의 수 N
M, N = map(int, input().split())
arr = list(map(int, input().split())) # 각 과자의 길이
arr.sort()
# print(arr)
# 모두에게 같은 길이의 막대 과자를 주어야 한다.
# 나누어진 막대과자의 길이는 합칠 수 없다
# 막대는 소수점으로 나눠질 수 없다. 반드시 정수형으로만 나눌 수 있다.
# 만족하는 과자 길이의 시작점을 찾아야 하므로, 이진탐색이 두 번 들어가야 한다.
print(bin_search())