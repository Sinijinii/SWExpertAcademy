'''N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.
입력
첫 줄에 테스트케이스 개수 T, 다음 줄부터 테스트케이스별로 첫 줄에 수열의 길이 N,
다음 줄에 N개의 0과1로 구성된 수열이 공백없이 제공된다.
1<=T<=10, 10<=N<=1000'''

T = int(input())
for tc in range(T):
    N = int(input())
    arr = str(input())
    cnt = 0
    result_list = []
    result = 0
    for num in arr:
        if int(num) == 1:
            cnt += 1
        else:
            if cnt != 0:
                result_list.append(cnt)
            cnt = 0
        result_list.append(cnt)
    for max_data in result_list:
        if result <= max_data:
            result = max_data
    print("#{}".format(tc+1), result)

