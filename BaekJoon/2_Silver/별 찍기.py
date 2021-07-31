import sys
sys.stdin = open('../input.txt', 'r')
def reculsive(n, nr, nc):
    if n == 3:
        for r in range(nr, nr+3):
            for c in range(nc, nc+3):
                if r == nr+1 and c == nc+1:
                    continue
                arr[r][c] = '*'
        return
    # 0, 0 위치는 나눗셈 오류나므로 그냥 호출
    for r in range(nr, nr+n, n//3):
        for c in range(nc, nc+n, n//3):
            if n // 3+nr == r and n // 3+nc == c:
                continue
            reculsive(n//3, r, c)

N = int(input())
# N * N 정사각형 모양으로 별 찍기
# 3의 패턴 : 가운데 공백, 그 외 모든칸에 별 하나
# 크기가 N일 경우 N/3 정사각형을 N/3 패턴으로 둘러싼 형태
arr = [list([' '] * N) for _ in range(N)]
reculsive(N, 0, 0)
for i in range(N):
    print(''.join(arr[i]))