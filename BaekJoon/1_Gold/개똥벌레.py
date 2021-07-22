import sys
sys.stdin = open("../input.txt", "r")

N, H = map(int, input().split()) # 동굴 길이 N, 높이 H
# 석순은 아래에서 자란 것, 종유석은 위에서 자란 것
arr = [int(input()) for _ in range(N)] # 장애물 높이 (석순, 종유석 반복)
top_arr, bottom_arr = [0]*(H+1), [0]*(H+1)
new_arr = [0]*(H) # 높이마다의 파괴를 담을 배열
for i in range(N):
    if i % 2: # 종유석
        top_arr[arr[i]] += 1
    else: # 석순
        bottom_arr[arr[i]] += 1
# 누적합 구하기
for i in range(H-2, 0, -1):
    top_arr[i] += top_arr[i+1]
    bottom_arr[i] += bottom_arr[i+1]

# 배열 정리
top_arr = top_arr[1:] # 조작해서 각 높이마다 몇개 깨는지 확인
bottom_arr = bottom_arr[1:][::-1] # 하나는 자른 뒤 역순으로 돌려준다

# 파괴량을 구해준다.
for i in range(H):
    new_arr[i] = top_arr[i]+bottom_arr[i]

new_arr.sort() # 가장 적은 파괴만 세기 위해 정렬
# 개수 세는 과정
res, cnt = new_arr[0], 1
for i in range(1, H):
    if new_arr[i] != res: break
    cnt += 1

print(res, cnt) # 출력