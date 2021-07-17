import sys
sys.stdin = open('../input.txt', 'r')

def bin_search(c):
    start, end = 0, L
    max_piece = 0
    while start <= end:
        tmp_piece = L
        last_one, cnt = 0, 0
        m = (start+end) // 2
        for i in range(M):
            length = spots[i]-last_one
            if length >= m:
                cnt += 1
                last_one = spots[i]
                if length < tmp_piece:
                    tmp_piece = length
        # 마지막 조각을 안 셌음
        if (L-last_one) < tmp_piece:
            tmp_piece = length

        if cnt >= c:
            start = m + 1
            if cnt == c and tmp_piece > max_piece:
                max_piece = tmp_piece
        else:
            end = m - 1
    return max_piece


N, M, L = map(int, input().split())
spots = [int(input()) for _ in range(M)]
cuts = [int(input()) for _ in range(N)]

for cut in cuts:
    result = bin_search(cut)
    print(result)
