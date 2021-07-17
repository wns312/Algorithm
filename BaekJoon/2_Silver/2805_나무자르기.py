import sys
sys.stdin = open('../input.txt', 'r')

def bin_search():
    low, high = 1, trees[-1]
    m = (low + high) // 2
    while low <= high:
        t_len = 0
        for i in range(N):
            if trees[i] > m:
                t_len += trees[i] - m
        if t_len == M: # 정확한 정답
            return m
        if t_len > M: # 너무 많이 잘랐다면 높이를 높인다
            low = m+1
        else: # 길이가 부족하다면 높이를 낮춘다
            high = m-1
        m = (low + high) // 2
    return m

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

result = bin_search()
print(result)