def f(pat, txt, M, N):
    for i in range(N-M+1):
        for j in range(M):
            if txt[i+j] != pat[j]:
                break
        else:
            return 1