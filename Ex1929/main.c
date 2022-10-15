 #include<stdio.h>
 #include<stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize){
    int *ans = (int*) malloc(numsSize*2*sizeof(int));
    *returnSize=2*numsSize;
    for(int i=0;i<numsSize; i++){
        ans[i]=nums[i];
        ans[i+numsSize]=nums[i];
    }
    return ans;
}