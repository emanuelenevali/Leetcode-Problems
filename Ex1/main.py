
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_={}
        for ind, val in enumerate(nums):
            if target-val in dict_:
                return dict_[target-val], ind
            dict_[val]=ind
