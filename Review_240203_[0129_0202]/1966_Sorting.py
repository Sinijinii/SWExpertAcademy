T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int,input().split()))

    # 버블정렬
    for bb in range(N-1, 0, -1):
        for j in range(bb):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print("#{}".format(tc+1),*arr)

    # 카운팅 정렬 -> 숫자의 범위가 나와있지 않아서 할 수 없으나 50으로 가정하고 진행
    counting = [0]*50
    temp = [0]*N

    for i in arr:
        counting[i] += 1
    # 누적합
    for i in range(1,N):
        counting[i] += counting[i-1]

    # 뒤에서부터 위치 좌표 할당
    for i in range(N-1,-1,-1):
        counting[arr[i]] -= 1
        temp[counting[arr[i]]] = arr[i]
    print(arr)
