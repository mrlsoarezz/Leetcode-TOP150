"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

"""

class Solution:
    
    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2
        self.m = 0
        self.n = 0
        

    def merge(self):
        s = 0
        for i in range(len(self.array1)):
            if self.array1[i] == 0:
                self.array1[i] = self.array2[s]
                s += 1
        return  self._Solution__sortIt()


        
    def __sortIt(self):
        for i in range(len(self.array1)):
            for q in range(len(self.array1)):
                if (self.array1[i] < self.array1[q]):
                    keep, self.array1[q] = self.array1[q], self.array1[i]
                    self.array1[i] = keep
        return self.array1
    

result = Solution([0], [1])

result.m = len(result.array1)
result.n = len(result.array2)

print(result.merge())


        
