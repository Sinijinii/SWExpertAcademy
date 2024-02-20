T = 10

def Postfix(N, data):
    top = -1
    stack = [0] * N
    isp = {'(': 0, '*': 2, '/': 2, "+": 1, "-": 1,0:0}
    res = ""
    for tk in data:
        if tk in "/*-+" and isp[stack[top]] < isp[tk]:
            top += 1
            stack[top] = tk

        else:
            res += tk
    res += stack[top]
    return res

def calculator(data_arr):
    i = 0
    try:
        while len(data_arr) != 1:
            if str(data_arr[i]) in '*/+-':
                if data_arr[i] == '*':
                    data_arr[i - 2] = int(data_arr[i - 2]) * int(data_arr[i - 1])
                    data_arr.pop(i - 1)
                    data_arr.pop(i - 1)
                    i = 0
                elif data_arr[i] == '/':
                    data_arr[i - 2] = int(data_arr[i - 2]) // int(data_arr[i - 1])
                    data_arr.pop(i - 1)
                    data_arr.pop(i - 1)
                    i = 0
                elif data_arr[i] == '+':
                    data_arr[i - 2] = int(data_arr[i - 2]) + int(data_arr[i - 1])
                    data_arr.pop(i - 1)
                    data_arr.pop(i - 1)
                    i = 0
                elif data_arr[i] == '-':
                    data_arr[i - 2] = int(data_arr[i - 2]) - int(data_arr[i - 1])
                    data_arr.pop(i - 1)
                    data_arr.pop(i - 1)
                    i = 0
            i += 1
    except:
        data_arr = '0'
    return data_arr


for tc in range(T):
    N = int(input())
    data = input()
    data = Postfix(N,data)
    data_sp = list(data)
    print(f'#{tc+1}',*calculator(data_sp))