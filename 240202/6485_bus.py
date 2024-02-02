'''삼성시에 있는 5,000개의 버스 정류장은 관리의 편의를 위해 1에서 5,000까지 번호가 붙어 있다.

그리고 버스 노선은 N개가 있는데, i번째 버스 노선은 번호가 Ai이상이고,

Bi이하인 모든 정류장만을 다니는 버스 노선이다.

P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램을 작성하라.'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    counts = [0] * 5001 #5000번 정류장
    # n개의 노선을 정류장에 표시
    for i in range(N):
        A, B = map(int,input().split())
        for j in range(A,B+1):
            counts[j] += 1
    P = int(input())
    bus_stop = [int(input()) for _ in range(P)]
    print("#{}".format(tc), end=" ")
    for i in bus_stop:
        print(counts[i],end = ' ')
    print()
