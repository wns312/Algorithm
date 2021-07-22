import sys
sys.stdin = open('../input.txt', 'r')

# 마지막 피스 계산 : 마지막 피스가 middle보다 작은 경우를 판단해야 한다.
# 만약 다 맞게 잘랐는데 마지막 피스가 middle보다 작아버리면??
# 그게 정답으로 갱신된다. 갱신되면 사이즈를 키워야 함

def bin_search(idx):
    left, right = 1, L
    res = 0
    while left <= right:
        middle = (left+right)//2
        min_piece = L
        last = 0
        cnt = 0
        for i in range(M):
            piece = cut_spot[i]-last
            if piece >= middle:
                last = cut_spot[i]
                cnt += 1
                if piece < min_piece:
                    min_piece = piece
        last_piece = L - last
        if last_piece < min_piece:
            min_piece = last_piece
        # 만약 cnt가 일치하고 가장 작은 조각이 결과보다 크면 갱신
        # 갱신이면 사이즈를 키워본다
        if cnt >= cut_cnt[idx]:
            res = min_piece
            left = middle + 1
        else:
            right = middle - 1
    return res


N, M, L = map(int, input().split()) # L은 케익 길이
cut_spot = [int(input()) for _ in range(M)] # 자르는 위치
cut_cnt = [int(input()) for _ in range(N)] # 몇 번 자를지
for i in range(N):
    print(bin_search(i))

# 1 1 1이라면?