import sys
sys.stdin = open('../input.txt', 'r')
# r, c 는 시작위치, l은 종이 길이
def reculsive(r, c, l):
    global cnt_w, cnt_b

    if l == 1: # 만약 종이 크기가 1이면
        cnt[arr[r][c]] += 1
        return

    # 종이 길이가 1이 아닐 때
    color = arr[r][c]
    for nr in range(r, r+l):
        for nc in range(c, c+l):
            if arr[nr][nc] != color: # 컬러가 통일되어있지 않다면?
                # 재귀 호출 네개!
                reculsive(r, c, l//2)
                reculsive(r+l//2, c, l//2)
                reculsive(r, c+l//2, l//2)
                reculsive(r+l//2, c+l//2, l//2)
                return # 재귀 호출하고나서 리턴해버린다
    # 여기까지 왔다면 종이가 완성이므로 color +=1
    cnt[color] += 1


N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]
cnt = [0, 0]
reculsive(0, 0, N)
# 0이 하얀색 색종이, 1이 파란색 색종이이다.
print(cnt[0], cnt[1])



# 9
# 7