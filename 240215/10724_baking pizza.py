from collections import deque
# 테스트 케이스
T = int(input())
for tc in range(T):
    # 화덕 크기 N, 피자 M
    N,M = map(int,input().split())
    # 피자의 치즈 양
    piz = deque(map(int, input().split()))
    # 딕셔너리로 변경(피자에 번호 부여) 키: 피자번호 / 데이터: 치즈의 양
    # > 1:7, 2:2, 3:6, 4:5
    piz_dic = {}
    for idx in range(M):
        piz_dic[idx+1] = piz[idx]
    # 피자번호 리스트 생성
    piz_num = [i for i in range(1,M+1)]
    # 처음 오븐에 들어가있는 피자, 들어가지 않은 피자
    oven = piz_num[:N]
    n_oven = piz_num[N:]
    oven = deque(oven)
    n_oven = deque(n_oven)

    # 오븐안의 피자가 있을 경우 > pop까지 하고 끝나기에 1이상이 아닌 초과
    while len(oven) > 1:
        # 피자가 입구에 오면 치즈의 양이 반
        piz_dic[oven[0]] = piz_dic[oven[0]] // 2
        # 만약 치즈의 양이 0이라면 오븐에서 꺼내줌
        if piz_dic[oven[0]] == 0:
            oven.popleft()
            # 이때 오븐에 안들어간 남은 피자가 있다면, 오븐에 넣어주기
            if len(n_oven) != 0:
                oven.appendleft(n_oven[0])
                n_oven.popleft()
        # 치즈의 양이 0보다 크다면 계속 회전하며 치즈양 확인
        else:
            oven.append(oven[0])
            oven.popleft()
    # 최종 값
    print(f"#{tc+1}",*oven)
