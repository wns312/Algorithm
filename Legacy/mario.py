
def get_max(idx, score):
    global result
    if idx > N:
        if result < score:
            result = score
        return

    if best[idx] < score:
        best[idx] = score

    if idx+2 < N+1 and best < score+arr[idx+2]:
        get_max(idx+2, score+arr[idx+2])
    if idx+7 < N+1 and best < score + arr[idx + 7]:
        get_max(idx+7, score+arr[idx+7])

N = 14
arr = [0, 1, 50, 1, -1, 1, 3, -1, 1, -15, 0, 100, 1, 1, 2]
result = 0
# 마리오가 얻을 수 있는 최고 점수
best = [0] * len(arr)
get_max(0, 0)
# 150