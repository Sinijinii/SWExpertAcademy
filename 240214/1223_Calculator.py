def calculator(lst):
    stack = []  # 피연산자 바로 추가할 리스트 생성
    if_stack = []
    #print(lst)
    for l in range(len(lst)):
        if str(lst[l]).isdigit():
            stack.append(lst[l])
        if len(stack) >= 2:
            if lst[l] == '+':
                a1 = stack.pop()
                a2 = stack.pop()
                stack.append(a1 + a2)
            elif lst[l] == '-':
                a1 = stack.pop()
                a2 = stack.pop()
                stack.append(a1 - a2)
            elif lst[l] == '*':
                a1 = stack.pop()
                a2 = stack.pop()
                stack.append(a1 * a2)
            elif lst[l] == '/':
                a1 = stack.pop()
                a2 = stack.pop()
                stack.append(a1 / a2)
        else:
            if str(lst[l]) in '*/-+':
                if_stack.append(lst[l])

        print(stack)


def Postfix(n, fx):
    postfix = []
    stack = []
    str =""
    for tk in fx:
        if tk.isdigit():
            postfix.append(int(tk))
            str += tk
        else:
            if stack:
                if isp[stack[-1]] < isp[tk]:
                    stack.append(tk)
                else:
                    while stack and isp[stack[-1]] >= isp[tk]:
                        a = stack.pop()
                        postfix.append(a)
                        str += a
                    stack.append(tk)
            else:
                stack.append(tk)

    while len(stack) > 0:
        a = stack.pop()
        postfix.append(a)
        str += a

    return postfix


T = 10
for tc in range(T):
    n = int(input())
    fx = input()
    isp = {'(': 0, '*': 2, '/': 2, "+": 1, "-": 1,0:0}
    #print(Postfix(n,fx))
    print(calculator(Postfix(n,fx)))