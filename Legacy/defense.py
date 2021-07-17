import sys
sys.stdin = open('defense.txt', 'r')


def defense(columns, enemies):  # 복사해온 enemies므로 문제없음
    cnt = 0
    r = N
    # target적용이 끝나면 적 리스트에서 적을 제거 후 제거 적 카운트
    # # 범위를 지나간 적은 그냥 리스트에서 제거

    for _ in range(N):  # 최대 N만큼 돌리면 존재하는 적이 모두 제거되거나 모두 이동됨
        target = list()  # 쏠 적이 들어갈 배열
        for c in columns: # 궁수의 위치는 r, c가 됨
            # 궁수 한명이 취할 행동을 여기에서 코딩
            # 1. 거리가 가장 적은 적을 찾는다. 혹은 거리가 같으면서 c가 적은 적을 찾는다
            scoped_enemies, min_d = list(), D
            for i in range(len(enemies)):
                er, ec = enemies[i]
                enemy_d = abs(r - er) + abs(c - ec)
                if enemy_d <= D and enemy_d <= min_d:
                    scoped_enemies.append((enemy_d, ec, er))
                    min_d = enemy_d
            scoped_enemies.sort()
            if scoped_enemies:
                target.append((scoped_enemies[0][2], scoped_enemies[0][1]))
        # target 제거 후, enemies 목록에서 target 제거 후, enemies의 row들 +1 해줌
        print(target)
        return







def set_archer_pos():  # 궁수의 위치를 잡고, defense 호출
    for b1 in range(M):
        for b2 in range(b1+1, M):
            for b3 in range(b2+1, M):
                pass
                # defense([b1, b2, b3], list(enemies))


for tc in range(1, int(input())+1):
    N, M, D = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    enemies = [(i, j) for i in range(N) for j in range(M) if arr[i][j]]
    enemies_num = len(enemies)  # 사용 여부 확인 후 폐기
    print(tc, enemies)
    # set_archer_pos()
    defense([0, 1, 2], list(enemies))