





# 문자삼각형 2
# while True:
#     N = int(input()) # 삼각형 높이
#     if 1 <= N <= 100 and N % 2: break
#     print("INPUT ERROR")
#
# M = N//2+1  # 삼각형 가로 길이
# arr = [list(['']*M) for _ in range(N)]
# a_num = 65
#
# for j in range(M-1, -1, -1):
#     start = N//2 - (M-j-1)
#     end = (N//2)+1 + (M-j-1)
#
#     for i in range(start, end):
#         arr[i][j] = chr(a_num)
#         a_num += 1
#         if a_num == 91:
#             a_num = 65
#
# for i in range(N):
#     print(' '.join(arr[i]))