import sys
sys.stdin = open("../input.txt", "r")

def bin_search():
    dif = abs(arr[0]+arr[1])
    res_a, res_b = arr[0], arr[1]
    # 돌면서 바로바로 갱신해주자
    for i in range(N-1):
        a = arr[i]
        b = arr[i+1]
        l, r = i+1, N-1
        while l <= r:
            m = (l+r) // 2
            new_dif = a + arr[m]
            if not new_dif: return a, arr[m] # 결과가 0이면 바로 리턴
            if new_dif > 0:
                r = m-1
            else:
                l = m+1
            if abs(new_dif) < abs(a+b): # 차이값을 확인해서 갱신해야지..아무떄나 갱신하면 안된다.
                b = arr[m]
        if abs(dif) > abs(a+b):
            res_a, res_b = a, b
            dif = abs(a+b)
    return res_a, res_b


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = bin_search()
print(result[0], result[1])
