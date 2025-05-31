class Solution(object):
    def removeDuplicates(self, nums):
        num = sorted(set(nums))

        k = len(num)

        for i in range(k):
            nums[i] = num[i]

        return k