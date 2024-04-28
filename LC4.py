# 4. Median of Two Sorted Arrays
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        arr=nums1+nums2
        arr.sort()
        n=len(arr)
        if n % 2 == 0: 
            return (arr[n//2 - 1] + arr[n//2]) / 2.0
        else:  
            return arr[n//2] / 1.0
        