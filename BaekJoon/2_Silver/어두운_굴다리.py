import sys
sys.stdin = open('../input.txt', 'r')
N = int(input()) # 굴다리 길이
M = int(input()) # 가로등 개수
arr = list(map(int, input().split())) # 가로등 위치
# 가로등의 높이가 H라면 왼쪽으로 H, 오른쪽으로 H만큼 비춘다 = 2H
start, end = 1, N
result = N
# start <= end여야 한다
# for-else문은 지양할 것 (뭔가 동작이 이상함 break되었는데도)
# dark_from같은거 밖에 넣는 실수 하지마라..
while start <= end:
    dark_from = 0
    m = (start+end) // 2 # 가로등 길이
    # 가로등 길이는 정했는데, 다 비췄는지에 대한 판별은?? 변수 저장
    for i in range(M):
        if arr[i]-m <= dark_from: # 잘 비춘 것
            dark_from = arr[i]+m
        else:
            break
    if dark_from < N:
        start = m+1
    else:
        end = m-1
        result = m
print(result)

