# def binarySearch(arr,N,key):
# 	start = 0
# 	end = N - 1
# 	while start <= end:
# 		middle = (start+end)//2
# 		if arr[middle] == key: return middle
#         elif arr[middle] > key:
#         end = middle - 1
#         else: start = middle +1
#     return -1 # 검색 실패



def selectionSort(arr,N):
    for i in range(N-1):
        minidx = i
        for j in range(i+1,N):
            if arr[minidx] > arr[j]:
                minidx = j
        # 최솟값을 구간 맨 앞으로 이동
        arr[minidx],arr[i] = arr[i],arr[minidx]
    return

N = 5
arr = [1,3,4,2,5]
print(arr)
selectionSort(arr,N)
print(arr)






# def select(arr,k):
#     for i in range(0,k):
#         minidx = i
#         for j in range(i+1,len(arr)):
#             if arr[minidx] > arr[j]:
#                 minidx = j
#         arr[i],arr[minidx] = arr[minidx],arr[i]
#     return arr[k-1]




