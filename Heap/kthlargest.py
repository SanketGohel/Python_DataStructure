
#Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the #sorted order, not the kth distinct element.

#Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which #contains initial elements from the stream. For each call to the method KthLargest.add, return the element #representing the kth largest element in the stream.






class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap =nums[0:k]
        self.k = k
        heapq.heapify(self.heap)
    
        
        for x in nums[k:]:
            if self.heap[0] < x: 
                heapq.heappushpop(self.heap, x)
        
        
        
        
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
            return self.heap[0]
        
        if self.heap[0] < val:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
