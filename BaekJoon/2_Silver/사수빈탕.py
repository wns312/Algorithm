import sys
sys.stdin = open("../input.txt", "r")

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
memo = [0]*N
for i in range(N): # 앞에서 뒤로 가면서 뒤에서 앞으로 탐색한다
    candy = M - (arr[i][0] + arr[i][1]) # 현재 좌표에서 얻을 수 있는 캔디 개수
    memo[i] = candy if candy > 0 else 0 # 현재값은 무조건 더할 것이므로 미리 더해둔다
    max_last_candy = 0 # 조건에 맞는 애들중 최대값을 저장하기 위한 변수
    for j in range(i-1, -1, -1):
        if arr[i][0] >= arr[j][0] and arr[i][1] >= arr[j][1]:
            if memo[j] > max_last_candy:
                max_last_candy = memo[j]
    memo[i] += max_last_candy # 더해준다
print(max(memo))