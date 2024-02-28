def pmt(x):
    if x == N-1:
        sum_data = 0
        sum_data += arr[0][pmt_list[0]]
        sum_data += arr[pmt_list[-1]][0]
        for i in range(len(pmt_list)-1):
            sum_data+=arr[i][i+1]
            sum_data += arr[i+1][i]
        print(sum_data)

        return
    for i in range(N-1):
        if used[i] == True:      # 추가: 이미 사용한 숫자인지 여부 확인
            continue
        used[i] = True           # 처음 사용이라면 숫자를 기록
        pmt_list.append(i+1)
        pmt(x+1)
        pmt_list.pop()
        used[i] = False          # 모든 처리가 끝나고 돌아온 후 기록 지움





T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    pmt_list = []
    used = list(0 for _ in range(N-1))
    pmt(0)