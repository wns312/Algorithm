import sys
sys.stdin = open('chip.txt', 'r')

def set_chip(sr, sc):
    global result
    for r in range(sr, H):
        # 여기가 문제, 모든 줄을 sc부터 시작하잖아. 다음줄은 1부터 시작해야함
        for c in range(sc, W):
            # print(r, c)
            # 걸어줘야 할 조건 : 1. 찍었을 때 기존의 찍혔던 개수보다 많은지(DP) (얘가 가장 앞에 와야함) 2. 벽이 있는지 3. 다른 웨이퍼랑 겹치는지
            # 1. 기존에 찍혔던 개수보다 많은지 검사
            if check[r][c] > len(chips)+1:
                return
            # 2. 벽이 있는지 검사
            if arr[r][c] or arr[r-1][c] or arr[r][c-1] or arr[r-1][c-1]: continue
            # 3. 다른 웨이퍼랑 겹치는지 검사
            for er, ec in chips:
                if (er+1 == r and ec+1 == c) or (er == r and ec+1 == c) or (er+1 == r and ec == c) or (er+1 == r and ec-1 == c):
                    break
            else:  # break에 걸리지 않은 경우 = 겹치지 않는다 = 놓을 수 있다
                chips.append((r, c))
                check[r][c] = len(chips)
                if len(chips) > result:
                    result = len(chips)
                if c+1 == W:
                    set_chip(r + 1, 1)
                else:
                    set_chip(r, c + 1)
                # 리턴되었으면 마지막 칩을 제거
                chips.pop(-1)
        # 한 줄이 끝났으면 0으로 만들어줌
        sc = 1


T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    check = [list([0]*W) for _ in range(H)] # 현재 칩 개수와 여기 찍힌 칩 개수가 같다면 더이상 진행하지 않는다 (DP)
    chips = list()
    result = 0
    set_chip(1, 1)
    print('#{} {}'.format(tc, result))


#1 9
#2 10
#3 0
#4 18
#5 12
