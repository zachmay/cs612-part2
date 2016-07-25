#include <stdio.h>

int step(int x)
{
    int i = 0;

    if ( x % 2 == 0 )
    {
        if ( x < 20 )
        {
            return x / 2;
        }
        else
        {
            return 6;
        }
    }
    else
    {
        i = 55;
    }

    if ( i == 0 )
    {
        return 3 * x + 1;
    }
    else
    {
        return 1;
    }
}

int main(int argc, char* argv[])
{
    int x;
    scanf("%d", &x);

    while ( x != 1 )
    {
        x = step(x);
        printf("%d\n", x);
    }
}
