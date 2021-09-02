import sys
sys.stdin = open('../input.txt', 'r')
while True:
    N = int(input())
    if not N: break
    words = [[input(), _] for _ in range(N)]
    lower_words = [[words[i][0].lower(), words[i][1]]for i in range(N)]
    lower_words.sort()
    print(words[lower_words[0][1]][0])
