import sys
sys.stdin = open('../input.txt', 'r')
N = int(input())
arr = list(map(int, input().split())) # 계산식
memo = [0] * 21
memo[arr[0]] = 1
cal_res = arr.pop() # 계산 결과
for i in range(1, N-1):  # 뒤를 pop했으므로 N-1까지 계산한다
    new_memo = list([0] * 21)  # 새로운 메모가 될 아이
    for j in range(21):  # 새 메모에 값을 할당해준다
        if not memo[j]: continue
        nums = [j+arr[i], j-arr[i]]
        for k in range(2):
            if 0 <= nums[k] <= 20:
                new_memo[nums[k]] += memo[j]
    memo = new_memo
print(memo[cal_res])
