import sys
sys.stdin = open("../input.txt", "r")

def bin_search():
    left, right = 0, max_value
    result = 0
    while left <= right:
        total = 0
        middle = (left + right) // 2
        for i in range(N):
            if city[i] < middle:
                total += city[i]
            else:
                total += middle

        if total == budget:
            return middle
        if total < budget:
            result = middle
            left = middle + 1
        else:
            right = middle - 1
    return result


N = int(input())
city = list(map(int, input().split()))
budget = int(input())
max_value = max(city)
if budget > sum(city):
    print(max_value)
else:
    print(bin_search())
