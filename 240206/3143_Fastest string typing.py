T = int(input())
for tc in range(T):
    A, B = input().split()
    A = A.replace(B,"B") # 해당 값을 한글자의 단어로 변경해줌
    print(f'#{tc + 1} {len(A)}')