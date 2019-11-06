class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            if left == right and target != nums[left]:
                return -1
            mid = left + (right - left)/2
            if target == nums[mid]:
                return mid
            if nums[mid] < nums[0]:
                if target >= nums[0] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] or target < nums[0]:
                    left = mid + 1
                else:
                    right = mid
            print('left is %s, right is %s'%(left, right))
        return -1