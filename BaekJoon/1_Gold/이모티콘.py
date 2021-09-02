import sys
sys.stdin = open('../input.txt', 'r')
N = int(input())
memo = [list([0]*N*2) for _ in range(N*2)]
memo[1][1], memo[2][1] = 1, 1
queue = [(2, 1)]  # 이건 계산해야될 애들을 넣은 배열
time = 2
while queue:
    size = len(queue)
    for i in range(size):
        emoji, clip = queue.pop(0)
        if emoji == N:
            queue, time = False, time-1
            break
        new_one = [(emoji, emoji), (emoji+clip, clip), (emoji-1, clip)]
        for j in range(3):
            if 0 < new_one[j][0] < (N*2) and 0 <= new_one[j][1] < (N*2) and not memo[new_one[j][0]][new_one[j][1]]:
                memo[new_one[j][0]][new_one[j][1]] = 1
                queue.append(new_one[j])
    time += 1
print(time)




