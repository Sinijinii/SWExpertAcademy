'''0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오.
카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
'''
T = int(input())
for tc in range(T):
    N = int(input())
    # 값을 str형으로 받아옴 - 인덱스 사용하기 위함
    arr = str(input())
    # 각 값의 갯수를 구할 리스트 생성
    count_list = []
    # 각 요소에 대한 count값 구하기
    for i in range(N):
        count = 0
        for j in range(N):
            if arr[i] == arr[j]:
                count += 1
        count_list.append(count)
    # 가장 많은 수를 가진 인덱스값 추출 *filter사용시 모든 인덱스 값을 가져올 수 있음
    max_idx = list(filter(lambda x : count_list[x] == max(count_list), range(N)))
    result = 0
    result_idx = 0
    # 가장 많은 수를 가진 인덱스 리스트를 순회하며 값을 비교 후 할당
    for idx in max_idx:
        if result < int(arr[idx]):
            result = int(arr[idx])
            result_idx = count_list[idx]
    print(f'#{tc+1} {result}{result_idx}')