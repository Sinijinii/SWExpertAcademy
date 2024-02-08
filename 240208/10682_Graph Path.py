'''
1
6 5
1 4
1 3
2 3
2 5
4 6
1 6
 '''
def dfs(i,Last,fin):
    vist = [0] * (Last + 1)
    st = []
    vist[i] =1
    result = 0
    while True:
        for w in adjl[i]:
            if vist[w] == 0:
                i = w
                st.append(i)
                vist[i] = 1
                break
        else:
            if st:
                i = st.pop()
            else: break

        if i == fin:
            result = 1
            break
        else: result = 0
    return result


T = int(input())
for tc in range(T):
    V,E = map(int, input().split())
    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        n1,n2 = map(int, input().split())
        adjl[n1].append(n2)
    S, G = map(int, input().split())
    print(f'#{tc+1} {dfs(S,V,G)}')
