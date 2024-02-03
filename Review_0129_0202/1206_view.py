T = 10
for tc in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    result = 0
    for i in range(N-4):    #N개의 건물중 맨 왼쪽 두칸과 오른쪽 두칸의 경우 건물이 없으므로 -4
        bul = max(arr[i],arr[i+1],arr[i+3],arr[i+4]) # 건물arr를 중심으로 왼쪽2, 오른쪽2중 가장 큰 값으로 비교
        if arr[i+2]-bul > 0:
            result += arr[i+2]-bul
    print(f'#{tc+1} {result}')