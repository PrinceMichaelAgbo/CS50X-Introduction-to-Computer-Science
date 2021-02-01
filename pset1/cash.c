/*#include <cs50.h>*/
#include <stdio.h>
#include <math.h>

int main(void) //main function to call other functions and print total number of coins
{
    float ask(void);
    int conversions(float);
    float change = ask();
    int coinnum = conversions(change);
    printf("%i\n", coinnum);
}

float ask(void)
{
    // keep asking until the right input is gotten
    float coins;
    do
    {
        coins = get_float("How much change is owed? ");
    }
    while (coins < 0); //there can't be negative change
    return coins;
}

int conversions(float change)
{
    // The coins conversions are done below
    int cents = round(change * 100); //geeting total cents
    int numquarters = cents / 25; //getting number of quarters
    int rem1 = cents % 25;
    int numdimes = rem1 / 10; //getting number of dimes
    int rem2 = rem1 % 10;
    int numnickels = rem2 / 5; //getting number of nickels
    int numpennies = rem2 % 5; //getting number if pennies
    // the total coin number
    int numcoins = numquarters + numdimes + numnickels + numpennies;
    return numcoins;
}
