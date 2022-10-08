

#include<stdio.h>

int removeElement(int* nums, int numsSize, int val){
    int k=numsSize;
    for(int i=0; i<k; i++){
        printf("%d\n", i);
        if(i==numsSize-1 && *(nums+i)==val){
            k--;
            break;
        }
        if(*(nums+i) == val){
            for(int j=i+1; j<numsSize; j++){
                *(nums+j-1) = *(nums+j);
            }
            k--;
            i--;
        }
        else{
            continue;
        }
    }
    return k;
}

int main(void){
    int nums[] = {3,2,2,3};
    int numsSize = 4;
    int val = 3;
    int k = removeElement(nums, numsSize, val);
    printf("\n%d\n", k);
    printf("%d,%d,%d,%d",nums[0],nums[1],nums[2],nums[3]);
    
   /* for(int i = 0; i<5; i++){
        printf("%d", i);
        if(val == 2 && i == 3 ){
            i--;
            printf("%d", i);
            val = val-1;
        }
    }
    */
    return 0;
}






