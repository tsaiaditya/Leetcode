class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.l=[]
        self.k=k
        self.start=0
        
    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        
        if self.isFull():return False
        self.l.append(value)
        return True
    
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():return False
        self.start+=1
        return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        
        return self.l[self.start] if not self.isEmpty() else -1
        
       

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        return self.l[-1] if not self.isEmpty() else -1
     

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return len(self.l)<=self.start
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return len(self.l)-self.start==self.k
