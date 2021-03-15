from Queue import Queue

def Cycle(N, queue):
    for i in range(N):
        queue.enqueue(queue.dequeue())
    return queue
