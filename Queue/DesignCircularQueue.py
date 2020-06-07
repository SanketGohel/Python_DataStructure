#Design your implementation of circular queue .The circular queue is a linear data structure in which the operation 
#are performed based on FIFO principle and the last position is connected back to the first position to make a circle.
 








class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0]*k
        self.head = 0
        self.tail = 0
        self.size = k

        
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        #print("size: " ,self.size)
        if self.size  == self.tail:
            #print("self of queue: ", self.size) 
            
            return False
        else:
            self.queue[(self.head + self.tail)% self.size] = value
            #print("Value in Queue: " ,self.queue)
            self.tail+=1
            
            #print("Value of tail", self.tail)
            return True
        
            
            
            
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.tail  == 0:
            return False
        else: 
            self.head = (self.head + 1) % self.size
            self.tail -=1
            return True
        
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.tail == 0:
            return -1
    
        return self.queue[self.head]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.tail == 0:
            return -1
        return self.queue[(self.head + self.tail -1 )% self.size] 
        
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.tail ==0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.tail ==self.size
        
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()