/*---------------------------------------------------------------------------*/
/*   
          Program file name : tritype.c
          Functions         : main
*/
/*---------------------------------------------------------------------------*/

/* include files */
#include<stdio.h>

/*---------------------------------------------------------------------------*/
/*   
          Function         : main
          Parameters       : none
          Input            : 3 integers : triangle sides
          Output           : type of triangle 
          Description      : MATCH IS OUTPUT FROM THE ROUTINE:
                                     TRIANG = 1 IF TRIANGLE IS SCALENE
                                     TRIANG = 2 IF TRIANGLE IS ISOSCELES
                                     TRIANG = 3 IF TRIANGLE IS EQUILATERAL
                                     TRIANG = 4 IF NOT A TRIANGLE 
*/
/*---------------------------------------------------------------------------*/



main()
{

    int i, j, k, triang;

    scanf("%d %d %d", &i, &j, &k);


    /*
       After a quick confirmation that it's a legal  
       triangle, detect any sides of equal length
*/

    if (( i <= 0 ) ||  (j <= 0)  ||  (k < 0))
    {
        triang = 4;
    }
    else
    {
        triang = 0;
        if (i == j) 
            triang += 1;
        if (i == k) 
            triang += 2;
        if (j == k) 
            triang += 3;

        if ( triang == 0)
        {

            /*
       Confirm it's a legal triangle before declaring
       it to be scalene
*/

            if ( i+j <= k  || j+k <= i  || i+k < j) 
                triang = 4;
            else 
                triang = 1;
        }
        else
        {
            /*
       Confirm it's a legal triangle before declaring
       it to be isosceles or equilateral
*/
            if (triang > 3) 
                triang = 3;
            else if (triang == 1 && i+j > k) 
                 triang = 2;
            else if (triang == 2 && i+k > j)
                 triang = 2;
            else if (triang == 3 && j+k > i)
                 triang = 2;
            else
                 triang = 4;
        }
    } 
    printf(" triang = %d\n", triang);

}
