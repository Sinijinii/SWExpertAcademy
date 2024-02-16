# # 삽입
# def enQueue(item):
#     global rear
#     if isFull():
#         print("QUEUE_FUll")
#     else:
#         rear += 1
#         Q[rear] = item
#
#
# # 삭제
# def deQueue():
#     global front
#     if isEmpty():
#         pass
#     else:
#         front += 1
#         return Q[front]
#
# # 공백 확인
# def isEmpty():
#     return front == rear
#
# # 포화상태 확인
# def isFull():
#     return rear == len(Q) - 1
#
# # 검색
# def Qpeek():
#     if isEmpty():
#         print("Queue_Empty")
#     else:
#         return Q[front + 1]

Q = []
front = -1
rear = -1

# 원형 큐
def isEmpty():
    return  front == rear
def isFull():
    return (rear+1)%len(Q) == front

# 원형 큐 삽입
def enQueue(item):
    global rear
    if isFull():
        print('QUEUE_FULL')
    else:
        rear = (rear + 1) % len(Q)
        Q[rear] = item

# 원형 큐 삭제
def deQueue():
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front = (front + 1) % len(Q)
        return Q[front]
