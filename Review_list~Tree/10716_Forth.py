from collections import deque
T = int(input())
for tc in range(T):
    arr = input().split()
    arr = arr[:-1]
    i = 0
    try:
        while len(arr) > 1:
            if str(arr[i]) in '*/+-':
                if arr[i] == "*":
                    arr[i-2] = int(arr[i-2]) * int(arr[i-1])
                    arr.pop(i-1)
                    arr.pop(i-1)
                    i = 0
                elif arr[i] == "+":
                    arr[i-2] = int(arr[i-2]) + int(arr[i-1])
                    arr.pop(i-1)
                    arr.pop(i-1)
                    i = 0
                elif arr[i] == "-":
                    arr[i-2] = int(arr[i-2]) - int(arr[i-1])
                    arr.pop(i-1)
                    arr.pop(i-1)
                    i = 0
                elif arr[i] == "/":
                    arr[i-2] = int(arr[i-2]) // int(arr[i-1])
                    arr.pop(i-1)
                    arr.pop(i-1)
                    i = 0
            else:
                i += 1

        print(f"#{tc+1}",*arr)
    except:
        print(f"#{tc+1}", 'error')
