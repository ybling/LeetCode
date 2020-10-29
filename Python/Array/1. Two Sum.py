# Leetcode Link: https://leetcode.com/problems/two-sum/submissions/
# 注意点：每个数字只可使用一次


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Method1(beat 15.2%, 4976 ms, O(n^2)): Brute Force 暴力解法
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):  # may not use the same element twice
                if nums[i] + nums[j] == target:
                    return [i,j]
        
        # Method2(beat 99.65%, 24ms): 使用dict
        nums_dict = {}
        for index, value in enumerate(nums):
            if target - value in nums_dict:
                return [index, nums_dict[target - value]]
            nums_dict[value] = index
        