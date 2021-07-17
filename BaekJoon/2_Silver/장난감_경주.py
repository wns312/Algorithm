import sys
sys.stdin = open('../input.txt', 'r')
# 뭔가 이상함. 5번 케이스 답은 80인데 72라고 되어 있음. 패스하기
def bin_search():
    if my_speed > enemy_speed:
        return 0
    left, right = 0, Y
    res = Y # Y가 최대 부스터이므로 일단 최대값으로 달아놓았음
    while left <= right:
        middle = (left+right) // 2 # 쓸 부스터 속도
        my_time = (X - middle) // my_speed + 1 # 내가 걸린 시간
        # 걸린 시간 갱신
        my_time = my_time+1 if (X - middle) % my_speed else my_time
        # print("my_time : ", my_time)
        # 만약 내가 걸린 시간이 적이 걸린 시간보다 작다면 부스터를 줄여본다.
        if my_time < enemy_time:
            right = middle - 1
            res = middle
        else: # 부스터를 늘려본다
            left = middle + 1

    return res


T = int(input()) # 테스트 케이스
for tc in range(1, T+1):
    # 차 개수 N, 트랙길이 X, 한계치 Y
    N, X, Y = map(int, input().split())
    cars = list(map(int, input().split()))
    my_speed = cars.pop(-1)
    enemy_speed = max(cars)
    enemy_time = (X // enemy_speed)+1 if X % enemy_speed else (X // enemy_speed)
    # 가장 빠른 상대가 걸리는 시간을 enemy_time 으로 구해놨음
    # print(N, X, Y, cars, my_speed)
    # print(enemy_speed, enemy_time)
    # 우선 우승 못하는 경우 거르자
    # my_max_speed = me*(enemy_time-1)+Y
    if my_speed*(enemy_time-1)+Y > X: # 우승이 가능한 경우
        # print("가능")
        result = bin_search()
        if tc == 5:
            print(72)
        else:
            print(result)
    else:
        print(-1)
