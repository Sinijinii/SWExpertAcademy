T = int(input())
for tc in range(T):
    A,B = input().split()
    print(f"#{tc+1}",len(A.replace(B," ")))