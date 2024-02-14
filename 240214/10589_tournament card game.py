# 그룹 나누기 함수(cut)
# 1 3 2 1 -> [[1,3],[2,1]]
def cut(arr):
    # 나누는 위치
    cut_p = (len(arr)+1)//2
    # cup_p == 2 -> 두개의 경우 비교를 해야함 > 최종 리스트에 추가
    if cut_p == 2:
        cut_list.append(arr[:cut_p])
        cut_list.append(arr[cut_p:])
    # cut_p == 1 -> 1개의 경우 단일로 올라감
    elif cut_p ==1:
        cut_list.append(arr)
    # 2보다 큰 경우에는 적어도 2이하로 잘라줌
    if cut_p > 2:
        cut(arr[:cut_p])
        cut(arr[cut_p:])
    return cut_list

# 가위바위보 함수
def rsp(arr,rsp_dict):
    # 그룹으로 나눈 값을 비교 -> [[1,3],[2,1]]
    for i in arr:
        # 사람별 낸 값을 가져오기
        values = list(map(rsp_dict.get, i))
        # 만약 비교값이 1,3이나 3,1로 되어 있는 경우엔 1이 승
        if values == [1,3] or values == [3,1]:
            win.append(i[values.index(1)])
        # 그렇지 않은 경우엔 큰 값을 낸 사람이 승
        else:
            win.append(i[values.index(max(values))])
    return win

T = int(input())
for tc in range(T):
    # 인원수
    N = int(input())
    # 사람별 낸 값
    value = list(map(int,input().split()))
    # 사람을 키로 낸 값을 데이터로 하는 딕셔너리 생성
    rsp_dict = {}
    for idx in range(N):
        rsp_dict[str(idx+1)] = value[idx]
    # 사람번호별 리스트 생성
    pp = list(rsp_dict.keys())

    # 최종 승리자가 나올때까지
    while len(pp) != 1:
        # 자른 값을 넣을 리스트
        cut_list = []
        # 각 토너먼트별 이긴사람을 담을 리스트
        win = []
        # 최종 이긴사람으로 변경
        pp = rsp(cut(pp),rsp_dict)

    print(f"#{tc+1}", *pp)

