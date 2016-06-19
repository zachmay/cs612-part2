#include <stdio.h>

// B5

int main(int argc, char *argv[])
{
    int i;
    scanf("%d", &i);
    if ( i == 1 ) // B4
    {
        printf("BLAH"); 
    } // B3
    else
    {
        i = 1; // B2
    }
    printf("%d", i);
} // B1
// B0

