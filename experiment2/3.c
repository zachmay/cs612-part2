#include <stdio.h>

int step(int x)
{
    if ( x % 2 == 0 )
    {
        return x / 2;
    }
    else
    {
        return 3 * x + 1;
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
