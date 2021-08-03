import sys
sys.stdin = open("../input.txt", "r")
memo = [1]+([0]*31)
cal_idx = 0
def pac(n, r):
    global cal_idx
    if n == r: # n-r이 0이면 1이다
        return 1
    # n이 무조건 더 크기 때문에 n만 구하면 된다
    if not memo[n]:
        memo[n] = memo[cal_idx] # 계산이 이미 된 값부터 시작해서 계산한다
        for i in range(cal_idx+1, n+1):
            memo[i] = i * memo[i-1] # 새로운 값을 메모한다
        cal_idx = n # 어디까지 메모되었는지 기록한다
    return memo[n] // (memo[n-r] * memo[r]) # 조합 리턴


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    print(pac(M, N))
