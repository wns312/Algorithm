import sys
sys.stdin = open("../input.txt", "r")
N= int(input())
# 한개 또는 세개였음
if N%2:
    print('SK')
else:
    print('CY')