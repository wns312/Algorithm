import sys
sys.stdin = open('../input.txt', 'r')
def pick_beer(lv):
    cnt, happiness = 0, 0
    for prefer, beer_lv in beers:
        if lv >= beer_lv:
            happiness += prefer
            cnt += 1
            if cnt == N:
                if happiness >= M:
                    return True
                else:
                    return False
    return False


def bin_search():
    global river_lv
    low, high = 1, max_lv
    while low <= high:
        m = (low+high) // 2
        is_good = pick_beer(m)

        if is_good:
            river_lv = m
            high = m-1
        else:
            low = m+1


N, M, K = map(int, input().split())
beers = [tuple(map(int, input().split()))for _ in range(K)]
beers.sort(reverse=True)

max_lv = 2**31
river_lv = -1

bin_search()
print(river_lv)

