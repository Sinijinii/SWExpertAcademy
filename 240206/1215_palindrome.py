T = 10
for tc in range(T):
    N = int(input())
    num = N // 2
    arr = [list(input()) for _ in range(8)]
    # 앞부분을 ori 회문인지 비교할 뒷 문장을 cp
    ori_i,cp_i,ori_j,cp_j = "","","",""
    # 최종 회문의 개수를 구할 result
    result = 0
    # 짝수인경우 인덱스의 수를 반절만큼만 뒤로, 홀수인 경우 반+1을 해줘야함 > aavaa
    if N % 2 == 0:
        cp_idx = num
    else:
        cp_idx = num + 1
    # 8*8배열을 순회
    for i in range(8): # 행방향
        for j in range(8-N+1): # 열방향 > 열-찾고자하는 문자열의 길이 + 1
            # 행을 돌때 문자열의 길이만큼 가줘야함
            # if 찾고자 하는 문자열6 and i ==0
            # arr[0][0],arr[0][1],arr[0][2] > arr[0][1], arr[0][2], arr[0][3]
            for idx in range(j, j + num):
                ori_i += arr[i][idx]         # 가로
                cp_i += arr[i][idx+cp_idx] # 비교문도 함께 저장
                ori_j += arr[idx][i]        #세로
                cp_j += arr[idx+cp_idx][i] # 비교문도 함께 저장
            # 총 개수 구하기
            if ori_i == cp_i[::-1]:
                result += 1
            if ori_j == cp_j[::-1]:
                result += 1
            # 문자열 초기화
            ori_i,cp_i,ori_j,cp_j = "","","",""
    print(f'#{tc+1} {result}')


