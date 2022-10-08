import collections
class Solution(object):
    @classmethod
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_list = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if i!=j and j!=k and i!=k and nums[i]+nums[j]+nums[k]==0:
                        tmp_list=[]
                        tmp_list.append(nums[i])
                        tmp_list.append(nums[j])
                        tmp_list.append(nums[k])
                        for check in res_list:
                            print(check)
                            if collections.Counter(check) != collections.Counter(tmp_list):
                                res_list.append(tmp_list)
        return res_list

a = [1,2,3,4,1,-2]
# print(collections.Counter(a))
print(Solution.threeSum(a))