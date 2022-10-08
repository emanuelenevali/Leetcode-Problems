// O(N^2)
#include<stdio.h>
#include<stdlib.h>
int removeDuplicates(int* nums, int numsSize){
    int k=numsSize;
    for(int i=0; i<k-1;i++){
        if(nums[i]==nums[i+1]){
            printf("i = %d, num[i] = %d\n", i, nums[i]);
            for(int j=i;j<numsSize-1;j++){
                nums[j]=nums[j+1];
            }
            k--;
            i--;
            printf("nums = %d, %d, %d, %d, %d, %d, %d, %d, %d ,%d \n", *nums, *(nums+1), *(nums+2), *(nums+3), *(nums+4), *(nums+5), *(nums+6), *(nums+7), *(nums+8), *(nums+9));
        }
    }
    return k;
}

int main(void){
    //int *v=malloc(sizeof(int)*10);
    //*v=1; *(v+1)=1; *(v+2)=2;
    int v[] = {0,0,1,1,1,2,2,3,3,4};
    printf("%d\n", removeDuplicates(v,10));
    printf("%d, %d, %d, %d, %d, %d, %d, %d, %d ,%d ", *v, *(v+1), *(v+2), *(v+3), *(v+4), *(v+5), *(v+6), *(v+7), *(v+8), *(v+9));
    //free(v);
    return 0;
}