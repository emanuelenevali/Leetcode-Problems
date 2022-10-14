//Inefficient solution O(N^2)
#include <string.h>
#include <stdio.h>
int longestValidParentheses(char *s){
    int best_len = 0;
    int count_open;
    int count_close;
    for(int i=0; i<strlen(s); i++){       
        int len = 0;
        count_open = 0;
        count_close = 0;
        if (s[i] == '('){
            len++;
            count_open++;}
        else
            continue;
        for(int j=i+1; j<strlen(s); j++){
            printf("open: %d,close: %d\n", count_open, count_close);
            if(count_close>count_open){
                len--;
                break;}
            else{
                if (s[i] == '('){
                    count_open++;
                    len++;}
                else{
                    count_close++;
                    len++;}
            }
        }
        if(len>best_len)
            best_len=len;
    }
    return best_len;
}



int main(void){
    char* s = "((((((((((((((((()";
    printf("\n\n\n%d", longestValidParentheses(s));
    return 0;
}