#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h> 

int main(void)
{
    int count = 0;
    int myNum;
    srand(time(0));
    int r = rand() % 100;
    //printf("%i\n", r);
    printf("Type a number: \n");
    scanf("%d", &myNum);
    while (count < 4)
    {
        if (myNum == r)
        {
            printf("You guessed correctly!\n");
            break;
        }
        else 
        {
            printf("Please try again: ");
            scanf("%d", &myNum);
            count = count + 1;
        }
    }
    if (count == 4)
    {
        printf("Sorry you did not win. The number was %i\n", r);
    }
    //clock_t end = clock();
    return 0;
}
