# Leetcode Link: https://leetcode.com/problems/subsets/submissions/



class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Method1 (beat 48.92%, 24 ms, O(n*2^n)): Cascading 级联
        ''' 
        nums = [1,2,3]
        (1): start with an empty list
                subsets = []
        (2): take 1 as consideration
                subsets = [[],[1]]
        (3): take 2 as consideration
                subsets = [[],[1],[2],[1,2]]
        (4): take 3 as consideration
                subsets = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        '''
        subsets = [[]]
        for num in nums:
            subsets += [curr + [num] for curr in subsets]
        return subsets