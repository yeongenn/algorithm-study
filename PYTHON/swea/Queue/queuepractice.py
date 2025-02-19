N = int(input())

queue = []
for n in range(N):
    order = input()
    x = 0
    if 'enqueue' in order:
        order, x = order.split()
    
    if order == 'enqueue':
        queue.append(int(x))
    elif order == 'dequeue':
        if len(queue) != 0:
            print(queue.pop(0))
        else: print(-1)
    elif order == 'size':
        print(len(queue))
    elif order == 'isEmpty':
        if len(queue) != 0:
            print(-1)
        else: print(1)
    elif order == 'front':
        if len(queue) == 0:
            print(-1)
        else: print(queue[0])
    elif order == 'rear':
        if len(queue) == 0:
            print(-1)
        else: print(queue[-1])