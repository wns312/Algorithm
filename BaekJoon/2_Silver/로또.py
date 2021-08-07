import sys
sys.stdin = open('../input.txt', 'r')

def reculsive(idx, pick):
    if pick == 6:
        for i in range(N):
            print(lotto[i], end=' ') if sel[i] else None
        print()
        return
    if idx == N: return
    # 만약 다 못모았다면
    sel[idx] = 1
    reculsive(idx+1, pick+1)
    sel[idx] = 0
    reculsive(idx+1, pick)

while True:
    lotto = input()
    if lotto[0] == '0': break
    N = int(lotto[0])
    lotto = list(lotto.split())[1:]
    sel = [0] * N
    reculsive(0, 0)
    print()
