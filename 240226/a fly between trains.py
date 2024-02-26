T = int(input())
for tc in range(T):
    D,A,B,F = map(int,input().split())
    T = D *F / (A + B)
    print(f"#{tc+1} {T}")