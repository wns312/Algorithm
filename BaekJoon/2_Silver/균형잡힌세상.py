import sys
sys.stdin = open('../input.txt', 'r')

while True:
    string = input()
    if string == '.': break
    stack = []
    result = 'yes'
    for i in range(len(string)):
        if string[i] == '(' or string[i] == '[':
            stack.append(string[i])
        elif string[i] == ')' or string[i] == ']':
            if stack and (stack[-1]+string[i] == '()' or stack[-1]+string[i] == '[]'):
                stack.pop()
            else:
                result = 'no'
                break
    if stack:
        result = 'no'
    print(result)
