#include <stdio.h>
#include <string.h>

struct key{
    char buff[15];
    int pass;
};

int main(void)
{
    
    struct key k; 

    printf("\n Enter the password : \n");
    gets(k.buff);

    if(strcmp(k.buff, "thegeekstuff"))
    {
        printf ("\n Wrong Password \n");
    }
    else
    {
        printf ("\n Correct Password \n");
        k.pass = 1;
    }

    if(k.pass)
    {
        printf ("\n Root privileges given to the user \n");
    }

    return 0;
}