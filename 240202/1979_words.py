''' X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를
출력하는 프로그램을 작성하라.'''

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = []
    for arr_data in range(N):
        arr.append(list(map(int,input().split())))
    # 가로 방향 , 세로방향:2
    counts = 0
    counts2 = 0
    reset_counts = 0
    reset_counts2 = 0
    # 총 결과 반환할 변수
    result = 0
    for i in range(N):
        for j in range(N):
            # 한줄이 끝나면 리셋해줘야하기에 한칸당 +1
            reset_counts += 1
            reset_counts2 += 1
    # 세로버전
            # 만약 0인데 그전까지가 N이면 result에 1을 할당하고 counts는 다시 리셋
            if arr[i][j] == 0:
                if counts == K:
                    result += 1
                    counts = 0
                # counts가 0이 아닌경우에도 0을 만나면 초기화 -> 1011의 경우
                elif counts != 0:
                    counts = 0
            # 1인 경우+1
            else: counts += 1
            #N번 만큼 돈 후 counts 확인 후 결과 반환, resetcount와 counts변수 초기화
            if reset_counts == N:
                reset_counts = 0
                if counts == K:
                    result += 1
                counts = 0
    # 세로 버전
            if arr[j][i] == 0:
                if counts2 == K:
                    result += 1
                    counts2 = 0
                elif counts2 != 0:
                    counts2 = 0
            else:
                counts2 += 1
            if reset_counts2 == N:
                reset_counts2 = 0
                if counts2 == K:
                    result += 1
                counts2 = 0
    print("#{}".format(tc), result)

