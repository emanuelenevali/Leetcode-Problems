class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret_list=[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    for q in range(k+1, len(nums)):
                        if nums[i]+nums[j]+nums[k]+nums[q]==target:
                            tmp = sorted([nums[i],nums[j],nums[k],nums[q]])
                            if (tmp in ret_list):
                                continue
                            else:
                                ret_list.append(tmp)
        
        return ret_list



class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret_list=[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    val = nums[i]+nums[j]+nums[k]
                    miss_val = target-val
                    if miss_val in nums and nums.index(miss_val)>k:
                        tmp = sorted([nums[i],nums[j],nums[k], miss_val])
                        if (tmp in ret_list):
                            continue
                        else:
                            ret_list.append(tmp)
                    else:
                        continue
        
        return ret_list



