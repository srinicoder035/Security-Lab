#include<stdio.h>
#include<string.h>
struct key {
    char buff[15];
    int pass;
};

int main()
{
    struct key k;
    gets(k.buff);
    if(strcmp(k.buff, "saran"))
        printf("wp");
    else {
        printf("cp");
        k.pass=1;
    }
    
    if(k.pass) {
        printf("ello");
    }
}       
