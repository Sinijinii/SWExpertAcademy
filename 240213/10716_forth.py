'''
Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다.
3 4 + .

코드
출력
4 2 / .
2
4 3 - .
1
'''

T = int(input())
for tc in range(T):
    data_arr = list(input().split())
    data_arr.pop()
    i = 0
    try:
        while len(data_arr) != 1:
            if str(data_arr[i]) in '*/+-':
                if data_arr[i] == '*':
                    data_arr[i - 2] = int(data_arr[i - 2]) * int(data_arr[i - 1])
                    data_arr.pop(i - 1)
                    data_arr.pop(i - 1)
                    i = 0
                elif data_arr[i] == '/':
                    data_arr[i-2] = int(data_arr[i-2]) // int(data_arr[i-1])
                    data_arr.pop(i-1)
                    data_arr.pop(i-1)
                    i = 0
                elif data_arr[i] == '+':
                    data_arr[i-2] = int(data_arr[i-2]) + int(data_arr[i-1])
                    data_arr.pop(i-1)
                    data_arr.pop(i-1)
                    i = 0
                elif data_arr[i] == '-':
                    data_arr[i-2] = int(data_arr[i-2]) - int(data_arr[i-1])
                    data_arr.pop(i-1)
                    data_arr.pop(i-1)
                    i = 0
            i += 1
        print("#{}".format(tc+1), *data_arr)
    except:
        print(f"#{tc+1} error")



