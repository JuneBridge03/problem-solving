class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def getIndexOfNums1(left, right, target):
            if right == left:
                return right
            if right - left == 1:
                return left + int(nums1[left] < target)
            mid = (left + right) // 2
            if nums1[mid] > target:
                return getIndexOfNums1(left, mid, target)
            else:
                return getIndexOfNums1(mid, right, target)
        
        N = len(nums1)

        i = 0

        for e in nums2:
            i = getIndexOfNums1(i, N, e)
            nums1 = nums1[:i] + [e] + nums1[i:]
            N += 1
        
        if N % 2 == 0:
            return (nums1[N // 2 - 1] + nums1[N // 2]) / 2
        else:
            return nums1[N // 2]