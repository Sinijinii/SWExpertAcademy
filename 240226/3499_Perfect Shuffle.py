T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(input().split())

    a = 0
    b = int(N // 2)

    result = []
    for i in range(len(arr)):
        if i % 2 == 0:
            print(arr[a])
            result.append(arr[a])
            a += 1

        else:
            print(arr[b])
            result.append(arr[b])
            b += 1
    print(f"#{tc+1}",*result)