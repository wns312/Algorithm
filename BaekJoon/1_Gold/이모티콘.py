import sys
sys.stdin = open('../input.txt', 'r')

# S = int(input())  # 보내려는 스마일 이모티콘 개수
# memo = [list() for i in range(S+1)]
# # S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최소값을 구하시오
# # 2 <= S <= 1000
# # 이제 돌면서 개수를 구하고, memo를 확인 한 후, 있으면 진행 X, 없으면 memo에 넣고 진행한다
# # S가 2일때를 고려해서 작성하자
# queue = [(1, 1)]
# time = 1
# while queue:
#     size = len(queue)
#     for i in range(size):
#         imo, clip = queue.pop(0)  # 이모티콘개수, 클립보드개수
#         # 여기서 개수가 일치한다면 탈출?
#         if clip in memo[imo]: continue  # 만약 이미 memo에 기록되어있다면 진행하지 않는다
#         memo[imo].append(clip)
#         # 세가지 경우의 수를 전부 실행 + 0개인 경우 거르기
#         if imo:
#
#
#     # 전부 실행하고 큐에 넣었다면 1초 증가
#     time += 1
# print(memo)
# print(time)






