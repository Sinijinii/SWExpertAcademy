T = int(input())
code = {"0001101":'0',
        "0011001":'1',
        "0010011":'2',
        "0111101":'3',
        "0100011":'4',
        "0110001":'5',
        "0101111":'6',
        "0111011":'7',
        "0110111":'8',
        "0001011":'9'}
for tc in range(T):
    data = []
    N,M = map(int,input().split())
    arr = [input() for _ in range(N)]
    for arr_data in arr:
        if arr_data.find('1') != -1:
            data = arr_data
            break
    # 뒤집어서 찾는게 편함/ 항상 마지막은 1로 끝
    data = data[::-1]

    # 최종 식을 담아줄 변수 result
    result = ""
    # 1로 시작하는 첫 인덱스
    st = data.index("1")
    # 인덱스를 기준으로 8개의 암호숫자들을 받아옴
    for i in range(8):
        # 1개의 암호에는 7개의 숫자
        new = data[st:st+7]
        # 숫자를 뒤집어서 result에 저장
        # -> 뒤집어져 있는 숫자이기에 다시 뒤집어서 암호코드에 비교
        result += code[new[::-1]]
        st += 7
    # 짝수와 홀수일때의 합을 구하기
    even = 0
    odd = 0
    for i in range(8):
        if i % 2 == 0:
            even += int(result[i])
        else:
            odd += int(result[i])
    # 홀수 * 3 + 짝수가 10의 배수일때는 그 값들을 다 더한값으로
    if (odd*3 + even) % 10 == 0:
        print(f"#{tc+1}",sum(list(map(int,list(result)))))
    else:
        print(f"#{tc+1}",0)




