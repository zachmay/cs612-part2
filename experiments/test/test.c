#include <stdio.h>

int main(int argc, char* argv[])
{
    int i, j, k;

    scanf("%d", &i);
    scanf("%d", &j);
    scanf("%d", &k);

    if ( i < j ) {
        if ( j < k ) {
            i = k;
        } else {
            k = i;
        }
    }

    printf("%d %d %d", i, j, k);
}
