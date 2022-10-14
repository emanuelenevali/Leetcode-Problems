#include<stdio.h>
int removeDuplicates(int* nums, int numsSize){
    int k=1;
    for(int i=1;i<numsSize;i++){
        if(nums[i]!=nums[i-1]){
            nums[k]=nums[i];
            k++;
        }
    }
    return k;}


int removeElement(int* nums, int numsSize, int val){
    int k = 0;
    for(int i=0;i<numsSize;i++){
        if(nums[i]!=val){
            nums[k]=nums[i];
            k++;
        }
    }
    return k;
}






