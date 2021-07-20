import sys
sys.stdin = open("../input.txt")

def bin_search():
    left, right = 10**-9, min(square)
    res = 10**-9
    for i in range(25000): # 왜?
        middle = (left + right) / 2 # A의 길이
        quantity = (L//middle) * (W//middle) * (H//middle) # 실제 들어가는 박스
        if quantity >= N:
            res = middle
            left = middle + (10**-9)
        else:
            right = middle - (10**-9)
    return res

square = list(map(int, input().split()))
N = square.pop(0)
L, W, H = map(int, square)
print(bin_search())


# 2.0