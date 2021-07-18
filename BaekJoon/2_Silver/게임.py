import sys
sys.stdin = open("../input.txt", "r")
# 나눗셈 -> 곱셈 을 하면서 생기는 실수의 오차 때문에 오답이 발생함
# 그렇다면, 정수형 계산으로만 구할 수 있는 방법이 없는가?
def bin_search():
    left, right = 1, X
    res = -1
    while left <= right:
        middle = (left + right) // 2
        new_rates = (Y + middle) * 100 // (X + middle)

        if new_rates > rates: # 승률 변화 O
            res = middle
            right = middle - 1
        else: # 승률 변화 X
            left = middle + 1
    return res

X, Y = map(int, input().split())
# 게임 횟수 X, 이긴 게임 Y, 승률은 직접 구한다.
# 승률이 변화하는 시점을 구하시오
# 승률
rates = Y*100 // X
if rates == 100:
    print(-1)
else:
    print(bin_search())

