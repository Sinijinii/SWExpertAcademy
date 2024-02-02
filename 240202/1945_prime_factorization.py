'''숫자 N은 아래와 같다.

N=2a x 3b x 5c x 7d x 11e

N이 주어질 때 a, b, c, d, e 를 출력하라.'''
T = int(input())
for tc in range(T):
    N = int(input())
    dt = [2,3,5,7,11] # 소인수분해를 하기 위해 나눌 인자
    result_list = []  # 나눈 갯수를 담기 위한 리스트
    for i in dt:
        counts = 0
        while N % i == 0:   # 나머지가 없을때만 돌기
            N = N/i
            counts += 1
        result_list.append(counts)
    print("#{}".format(tc+1), *result_list)

