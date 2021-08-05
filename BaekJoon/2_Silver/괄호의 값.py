import sys
sys.stdin = open('../input.txt', 'r')

def get_res():
    stack = list()
    while string:
        # print(stack)
        letter = string.pop(0)
        if letter == '(' or letter == '[':
            stack.append(letter)
        else:
            if not stack: return 0 # 닫는 괄호인데 스택에 아무것도 없다면 리턴
            total = 0
            while stack:
                popped = stack.pop(-1) # 닫는 괄호여서 뽑은 것
                if str(popped) not in '()[]': # 스택에 있는게 숫자라면
                    total += int(popped)
                else: # 스택에 있는게 숫자가 아니라면 ( 또는 [ 이다
                    letters = popped+letter

                    if letters == '()':
                        if not total:
                            total = 1
                        total = total * 2
                        break
                    elif letters == '[]':
                        if not total:
                            total = 1
                        total = total * 3
                        break
                    else: # 페어가 맞지 않다면?
                        return 0
                if not stack and (letter == ']' or letter == ')'):
                    return 0
            stack.append(total)
    res = 0
    while stack:
        popped = stack.pop(0)
        if str(type(popped)) == "<class 'str'>":
            return 0
        res += popped
    return res

string = list(input())
tmp = 0
result = get_res()
print(result)
# 28