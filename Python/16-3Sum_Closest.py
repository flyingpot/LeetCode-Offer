class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in xrange(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sums = nums[i] + nums[l] + nums[r]
                if sums == target:
                    return sums
                if abs(sums - target) < abs(result - target):
                    result = sums
                if sums < target:
                    l += 1
                if sums > target:
                    r -= 1
        return result
