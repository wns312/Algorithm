import sys
sys.stdin = open('../input.txt', 'r')

def check_pixel(size):
    cnt = 0
    c = 0
    while c < COL:
        for r in range(ROW):
            if arr[r][c]:
                # 만약에라도 넘어가지 않도록
                x = c if c + size <= COL else COL - size





for tc in range(1, int(input())+1):
    ROW, COL = map(int, input().split()) # 백만 이하
    p_cnt = int(input()) # 색종이 장수 100 이하
    wrong_pixel = int(input()) # 잘 못 칠한 칸수 1000이하
    arr = [list([0]*COL) for _ in range(ROW)]
    for _ in range(wrong_pixel):
        y, x = map(int, input().split())
        arr[y-1][x-1] = 1
    # 도화지 출력
    for i in range(ROW):
        print(arr[i])


