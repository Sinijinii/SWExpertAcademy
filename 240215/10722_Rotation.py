from collections import deque
T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    arr = deque(map(int,input().split()))
    rear = 0
    for i in range(M):
        arr.append(arr[0])
        arr.popleft()
    print(f"#{tc+1}", arr[0])