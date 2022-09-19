#include<stdio.h>
double myPow(double x, int n){
//    printf("x: %lf\tn: %d\n", x, n);
    double res=1;
    if(x==0)
        return 0;
    if(n==0 || x ==1)
        return 1;
    if(n==-1)
        return 1/x;
    if(n%2==0)
        return myPow(x, n/2)*myPow(x, n/2);
    else
        return x*myPow(x,(n-1)/2)*myPow(x,(n-1)/2);
}

int main(void){
    double x=10;
    int n=-2;
    double res = myPow(x, n);
    printf("%lf", res);
    return 0;
}