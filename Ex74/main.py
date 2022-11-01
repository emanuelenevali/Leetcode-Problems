class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(arr: List[int], target: int, flag: int) -> int:
            left=0
            right=len(arr)-1
            while(left<=right):
                mid=int((left+right)/2)
                if target>arr[mid]:
                    left=mid+1
                elif target<arr[mid]:
                    right=mid-1
                else: return mid
            if flag == 0: return right
            else: return -1

        def findRow(matrix:List[List[int]], target: int) -> int:
            rowFirstValues=[]
            for i in range(len(matrix)):
                rowFirstValues.append(matrix[i][0])
            return binarySearch(rowFirstValues, target, 0)

        if len(matrix)==0: return False
        row_ind = findRow(matrix, target)
        ret = binarySearch(matrix[row_ind], target, 1)
        if ret==-1: return False
        else: return True