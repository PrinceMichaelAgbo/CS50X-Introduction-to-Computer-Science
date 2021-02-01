#include <cs50.h>
#include <stdio.h>


int main(void)
{
    int height, a, b, lines;
    do
    {
        // get user input of positive number less than or equal to 8
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (lines = 0; lines < height; lines++)
    {
        //print the appropriate number of spaces
        for (a = height - 1; a > lines; a--)
        {
            printf(" ");
        }
        //print the pound signs on the left
        for (b = -1; b < lines; b++)
        {
            printf("#");
        }
        printf("  "); //print the middle space
        for (b = -1; b < lines; b++)//print the pound signs on the right
        {
            printf("#");
        }
        printf("\n");//next line
    }
}

