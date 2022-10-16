int calPoints(char ** operations, int operationsSize){
    int *res=malloc(sizeof(int)*operationsSize);
    int valid_ind=0;
    for(int i=0; i<operationsSize; i++){
        if(*operations[i]!='+'&&*operations[i]!='D'&&*operations[i]!='C'){
            res[valid_ind]= atoi(operations[i]);
            printf("\n%d, %d ",i,res[valid_ind]);
            valid_ind++; }
        if(*operations[i]=='D'){
            res[valid_ind]=2*res[valid_ind-1];
            printf("\n%d, %d ",i,res[valid_ind]);
            valid_ind++; }
        if(*operations[i]=='C'){
            valid_ind--;
            printf("\n%d, %d ",i,res[valid_ind]); }
        if(*operations[i]=='+'){
            res[valid_ind]=res[valid_ind-1]+res[valid_ind-2];
            printf("\n%d, %d ",i,res[valid_ind]);
            valid_ind++;}}
    int sum=0;
    for(int i=0;i<valid_ind;i++){
        sum+=res[i]; }
    free(res);
    return sum;
}