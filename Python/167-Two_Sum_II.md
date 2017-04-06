简单，有序数组，使用双指针，注意根据题意返回的是indice加一。跟下面的比，我的代码写的太丑了。。。

答案：
```Python
# two-pointer
def twoSum1(self, numbers, target):
    l, r = 0, len(numbers)-1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1, r+1]
        elif s < target:
            l += 1
        else:
            r -= 1

# dictionary           
def twoSum2(self, numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target-num in dic:
            return [dic[target-num]+1, i+1] #注意先存在dic中的indice较小，根据题意，小的要在前面
        dic[num] = i

# binary search        
def twoSum(self, numbers, target):
    for i in xrange(len(numbers)):#注意Python3中已经没有xrange，Python3中的range就是Python2的xrange
        l, r = i+1, len(numbers)-1
        tmp = target - numbers[i]
        while l <= r:
            mid = l + (r-l)//2
            if numbers[mid] == tmp:
                return [i+1, mid+1]
            elif numbers[mid] < tmp:
                l = mid+1
            else:
                r = mid-1
```
