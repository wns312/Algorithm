import sys
sys.stdin = open("../input.txt")

def bin_search_to_start(idx, p):
    start, end = 0, idx-1
    m_position = bales[idx] - p # 이 거리보다 작으면 안터짐

    # 딱 맞지 않을 수도 있잖아
    while start <= end:
        m = (start + end) // 2

        if bales[m] == m_position:
            return m

        if bales[m] > m_position:
            end = m - 1
        else:
            start = m + 1
    return -1  # 못찾은 것 = 터트릴 수 있는게 없음
# 일단 앞으로만 터지는거 구해보기

def bin_search_to_end(idx, p):
    start, end = idx+1, N-1
    m_position = bales[idx]+p # 최대 m_position 숫자까지 터질 수 있음
    while start <= end:
        m = (start+end)//2

        if bales[m] == m_position:
            return m

        if bales[m] > m_position: # 멀리있으므로 더 가깝게 조정
            end = m-1
        else:
            start = m+1
    return -1 # 못찾은 것 = 터트릴 수 있는게 없음


# 거리 안에 있으면 무조건 다 터지는 걸로 계산하는게 맞아 보임
def explode(idx):
    power = 1
    end_p = bin_search_to_end(idx, power) # 터지는 위치를 리턴한다
    if end_p == -1:
        print("터트릴 게 없습니다")
    else:
        print(end_p)



N = int(input())
bales = [int(input()) for _ in range(N)]
bales.sort()
print(N, bales)
# bales에 적혀진 숫자가 포지션 같음
# 최대로 부술 수 있는 bales를 구하시오
max_explode = 0
explode(3)
# for i in range(N):
#     explode(i)



