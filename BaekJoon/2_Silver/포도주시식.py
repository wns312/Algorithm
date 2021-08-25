import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
arr = [int(input()) for _ in range(N)]
# 최대 연속 2잔만 가능하다
# print(arr)
m_0, m_1, m_2 = 0, arr[0], 0
max_n = 0
for i in range(1, N):
    m_0, m_1, m_2 = m_2, m_0+arr[i], max(m_1+arr[i], m_2)
    max_n = max(max(m_0, m_1, m_2), max_n)
print(max_n)


