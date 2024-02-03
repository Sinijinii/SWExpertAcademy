T = int(input())
for tc in range(T):
    arr = str(input())
    count_list = [0]*10     # 0~9까지 각 개수를 구하기 위한 0~9까지의 0으로 채워진 리스트
    result = 0              # Baby gin의 조건에 해당하는 result의 값 구함
    fin_result = 'Lose'     # 해당하지 않을 경우 : Lose
    # 0~9까지 각 개수를 구하기
    for count in arr:
        count_list[int(count)] += 1

    # 1번부터 10번까지 만약 갯수가 3보다 큰것이 있다면 result에 +1해주고, 해당 값은 제거
    # 만약 3보다 작다면 다음 인덱스로 넘어가기 위한 +1 과정 필요
    # while문 필요 이유 : 주어진 숫자가 333333인 경우 for문은 다음 인덱스로 자동 넘어가기 때문에
        # while문을 사용하여 특정 조건에서만 다음 인덱스에 접근할 수 있도록
    idx_1 = 1
    while idx_1 < len(count_list):
        if count_list[idx_1] >= 3:
            count_list[idx_1] -= 3
            result += 1
        else: idx_1 += 1

    # 연속하는 값의 갯수가 0개가 아니라면(초과) result에 +1해주고, 해당 값에 대해서는 -1
    # 만약 해당하지 않는다면 다음 인덱스로
    # while문 필요 이유 : 주어진 숫자가 123123인 경우 for문은 다음 인덱스로 자동 넘어가기 때문에
    # while문을 사용하여 특정 조건에서만 다음 인덱스에 접근할 수 있도록
    idx_2 = 1
    while idx_2 < 8:
        if count_list[idx_2] != 0 and count_list[idx_2+1] != 0 and count_list[idx_2+2] != 0:
            count_list[idx_2] -= 1
            count_list[idx_2+1] -= 1
            count_list[idx_2+2] -= 1
            result += 1
        else:
            idx_2 += 1

    if result == 2:
        fin_result = 'Baby Gin'
    print(f'#{tc + 1} {fin_result}')

    # for i in arr:
    #     count = 0
    #     if arr.find(str(int(i)+1)) != -1:
    #         if arr.find(str(int(i)+2)) != -1:
    #             result = 'Baby Gin'
    #             arr = arr.replace(str(int(i) + 1),"")
    #             arr = arr.replace(str(int(i)+2),"")
    #             arr = arr.replace(str(int(i)), "")
    # print(arr)
    # for i in arr:
    #     for j in arr:
    #         if i == j:
    #             count += 1
    #     count_list.append(count)
    # for idx in count_list:
    #     if idx >= 3:
    #         result = 'Baby Gin'
    #         break
    # print(f'#{tc + 1} {result}')