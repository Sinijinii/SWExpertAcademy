T = 10
for tc in range(T):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    h = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N + 1)
    for i in arr:
        h[int(i[0])] = i[1]
        if len(i) == 4:
            left[int(i[0])] = int(i[2])
            right[int(i[0])] = int(i[3])

    for i in range(N,-1,-1):
        if left[i] == 0:
            pass
        else:
            if str(h[i]) in '+-*/':
                if str(h[i]) == "+":
                    h[i] = int(h[left[i]]) + int(h[right[i]])
                if str(h[i]) == "-":
                    h[i] = int(h[left[i]]) - int(h[right[i]])
                if str(h[i]) == "*":
                    h[i] = int(h[left[i]]) * int(h[right[i]])
                if str(h[i]) == "/":
                    h[i] = int(h[left[i]]) / int(h[right[i]])
    print(f"#{tc+1}",int(h[1]))