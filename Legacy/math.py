def pick_max_q(idx):

    if idx == N:
        # 배열 비교
        a, b = list(), list()
        for i in range(N):
            if sel[i]:
                a.append(i+1)
                b.append(arr[i])
        if a == b:
            result = a
        return
    sel[idx] = 1
    pick_max_q(idx+1)
    sel[idx] = 0
    pick_max_q(idx+1)



N = int(input())
arr = [int(input()) for _ in range(N)]
print(arr)
sel = [1]*N
result = list()
