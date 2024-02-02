t = int(input())    # 테스트 케이스 개수 받기
 
for tc in range(1, t+1) :
    n, k = map(int, input().split())    # 단어 퍼즐의 가로, 세로 길이인 n과 단어의 길이 k
    arr = [list(map(int, input().split())) + [0] for _ in range(n)] + [[0]*(n+1)]
    # 2차원 퍼즐 모양을 받아준다. # +) 그 뒤 행과 열에 0만 들어있는 배열을 추가해준다...
    n += 1  # 0 인 열과 행 추가
 
    # 가로, 세로로 연속한 1의 개수가 k인 경우의 수를 찾아야 한다.
    ans = 0
    for i in range(n) :
        cnt = 0 # i행에서 연속한 1의 개수를 샐 카운트 변수 생성
        for j in range(n) :
            if arr[i][j] :
                cnt += 1
            else :  # arr[i][j] == 0 이면
                if cnt == k :
                    ans += 1
                cnt = 0
 
    for j in range(n) :
        cnt = 0 # j행에서 연속한 1의 개수를 샐 카운트 변수 생성
        for i in range(n) :
            if arr[i][j] :
                cnt += 1
            else :  # arr[i][j] == 0 이면
                if cnt == k :
                    ans += 1
                cnt = 0
 
 
    print(f'#{tc} {ans}')