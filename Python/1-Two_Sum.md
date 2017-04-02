简单，brutal force轻松AC。但是要注意题目要求“you may not use the same element twice”，开始没主意。

讨论区精彩解法:
```Python
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
```
使用字典的key存储需要的加数，value存储indice
