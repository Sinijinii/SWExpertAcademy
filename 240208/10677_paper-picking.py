def paper(n):
    if n < 2:  # N이 0일때와 10일때엔 경우의 수가 1개씩 나온다
        return 1
    else:
        return paper(n - 1) + 2 * paper(n - 2)


t = int(input())  # 테스트 케이스 개수 받기

for tc in range(1, t + 1):
    N = int(input())  # 20 x N 에서 N의 값을 받기
    n_simple = N // 10  # 계산을 쉽게 하기 위해 10 나누기를 합쉬다~~
    ans = paper(n_simple)

    print(f'#{tc} {ans}')