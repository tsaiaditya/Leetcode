import collections

class MovingAvg:
    def __init__(self,size):
        self.size = size
        self.queue = collections.deque()
    
    def next(self,value) -> float:
        if len(self.queue) == self.size:
            self.queue.popleft()
        self.queue.append(value)
        return sum(self.queue)/len(self.queue)

print("Enter the window size of moving average: ")
n = int(input())
m = MovingAvg(n)
print("Enter the values for the window and get the average as and when input is given: ")
while(True):
    x = int(input())
    print(m.next(x))