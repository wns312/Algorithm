import sys
sys.stdin = open("../input.txt", "r")

def bin_search():
    # 다 분배가 되었는지도 확인이 필요하다
    left, right = 1, 10**9
    envy = 10**9
    while left <= right:
        students = N
        middle = (left + right) // 2 # 나눠 줄 보석의 개수
        for i in range(M): # 여기서 보석을 하나씩 꺼내서 분배함
            jewel = arr[i] # 몫 나머지 연산
            students -= jewel // middle
            if jewel % middle:
                students -= 1
                if students < 0:
                    break
        if students < 0: # 보석이 남은 것
            left = middle + 1
        else: # 보석이 남지 않은 것 -> 결과에 반영
            right = middle - 1
            envy = middle
    return envy


N, M = map(int, input().split())
arr = [int(input()) for _ in range(M)]
# 학생들은 같은 색 보석만 가져가며, 보석은 모두 나누어 주어야 한다.
# 질투심이 최소가 되는 보석 분배를 하고, 그 때의 질투심 최대값을 구하시오
# 최대한 비슷하게 나누어 주어야 한다.
# 나누어 줄 보석의 개수가 이진 탐색의 대상이 된다.
print(bin_search())
