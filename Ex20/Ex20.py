class Solution(object):
    @classmethod
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_list = []
        old_number = None
        for i in nums:
            if i != old_number:
                temp_list.append(i)
                old_number = i
            else:
                continue
        for i in range(len(temp_list)):
            nums[i] = temp_list[i]
        return len(temp_list)

nums = [1, 1, 2]
print(nums[:Solution.removeDuplicates(nums)])
