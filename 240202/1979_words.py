''' X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를
출력하는 프로그램을 작성하라.'''

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = []
    for arr_data in range(N):
        arr.append(list(map(int,input().split()))+[1])
    arr.append([1]*(N+1))
    counts = 0
    counts2 = 0
    reset_counts = 0
    reset_counts2 = 0
    result = 0
    for i in range(N):
        for j in range(N):
            reset_counts += 1
            if arr[i][j] == 1 and arr[i+1][j+1] == 1:
                counts += 1
            else :
                counts = 0
            if reset_counts == N+1:
                reset_counts = 0
                if counts == K:
                    result += 1
                counts = 0
            if arr[j][i] == 1:
                counts2 += 1
            if reset_counts2 == N+1:
                reset_counts2 = 0
                if counts == K:
                    result += 1
                counts2 = 0

            print(counts)
