class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in xrange(len(nums) - 3):
            for j in xrange(i + 1, len(nums) - 2):
                k, l = j + 1, len(nums) - 1
                while k < l:
                    sums = nums[i] + nums[j] + nums[k] + nums[l]
                    if sums < target:
                        k += 1
                    elif sums > target:
                        l -= 1
                    else:
                        res.append((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
        return list(set(res))
