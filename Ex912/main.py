# Implementation of merge sort (not randomized)
# time complexity: O(n*logn)
# space complexity: O(n)

class Solution:   
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums1:List[int], nums2:List[int]) -> List[int]:
            nums=[]
            i1=0
            i2=0
            for i in range(len(nums1)+len(nums2)):
                if i1==len(nums1): 
                    nums.append(nums2[i2])
                    i2+=1
                    continue
                if i2==len(nums2):
                    nums.append(nums1[i1])
                    i1+=1
                    continue
                if nums1[i1]<=nums2[i2]:
                    nums.append(nums1[i1])
                    i1+=1
                    continue
                if nums1[i1]>nums2[i2]:
                    nums.append(nums2[i2])
                    i2+=1
            return nums
        if (len(nums)<=1): return nums
        mid=int((len(nums))/2)
        return merge(self.sortArray(nums[0:mid]), self.sortArray(nums[mid:]))