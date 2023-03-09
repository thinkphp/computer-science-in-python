#
# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
#

class Solution:

    def search(self, nums, target, lo, hi) -> int:
        if lo > hi:
            return lo
        m = (lo + hi) >> 1
        if target == nums[m]:
            return m
        elif target < nums[m]:
            return self.search(nums, target, lo, m - 1)
        else:
            return self.search(nums, target, m+1, hi)

    def searchInsert(self, nums, target) -> int:
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        return self.search(nums, target, 0, len(nums)-1)

nums = [1,3,5,6]

ob = Solution()
print(ob.searchInsert(nums, 5))
