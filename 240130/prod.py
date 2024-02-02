T = int(input())
for tc in range(T):
    N,N2 = map(int,input().split())
    data = list(map(int,input().split()))
    data2 = list(map(int, input().split()))
    sort_len = min(N,N2)
    max_len = max(N,N2)
    result = []
    i = 0
    for tc in range(abs(N2-N)+1):
        sum = 0
        for srt in range(i,i+sort_len):
            print(srt)
            sum += data[srt]*data2[srt]
        if  i+sort_len+1 <= max_len:
            i+=1
        result.append(sum)
    print(result)
