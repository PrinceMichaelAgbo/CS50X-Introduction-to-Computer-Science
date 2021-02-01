//#include <cs50.h>
#include <stdio.h>
#include <stdbool.h>

int main(void)// main function to call other functions
{
    long long ask(void);
    int checklength(long long);
    int luhn(long long, int);
        
    long long crednum = ask();
    int length = checklength(crednum);
    int end = luhn(crednum, length);
}

//function asks for the right input
long long ask(void)
{
    long long crednum;
    do
    {
        //crednum = get_long("Number: ");
        printf("Credit Card Number: ");
        scanf("%lli", &crednum);
        printf("%lli\n", crednum);
    }    
    while (crednum < 0);
    return crednum;
}

// function below calculates the length of the creditcard number
int checklength(long long crednum)
{
    long long rem = crednum;
    int counter = 0;
    
    while (rem != 0)
    {
        rem = rem / 10;
        counter ++;
    }
    return counter;           
}

// function below calculates Luhn's algorithm and the type of credit card
int luhn(long long creditnum, int length)
{
    bool validation(int);
    bool valid;
    long long prodigits, multby2, rem, n = creditnum;
    int firstnum, secondnum, sum, notmult, notmultotal = 0, addeveryother = 0;
    while (n != 0) // get each second number right to left
    {
        rem = (n % 100); 
        multby2 = (rem / 10) * 2; //the numbers that will be multiplied by 2
        notmult = (rem % 10);//the numbers that will not be multiplied by 2
        notmultotal += notmult;// add the numbers not multiplied by 2
        prodigits = (multby2 / 10) + (multby2 % 10);
        addeveryother += prodigits; //add the digits of the numbers multiplied by 2
        n /= 100;
        if ((n >= 100) & (n < 1000) & (length % 2 != 0))//400
        {
            secondnum = (n % 100) / 10; //get the second number if card number length is odd
        }
        if (n == 0)
        {
            if (length % 2 == 0) 
            {
                firstnum = rem / 10; //get the first number if card number length is even
                secondnum = rem % 10; //get the second number if card number length is even
            }
            else 
            {
                firstnum = rem; //get the first number if card number length is odd
            }
        }
    }
    sum = addeveryother + notmultotal;
    valid = validation(sum); //check if the card number is valid
    // below are just the conditions for each type of credit card
    if (valid == true)
    {
        if ((length == 15) & (firstnum == 3) & (secondnum == 4 || secondnum == 7))
        {
            printf("AMEX\n");
        }
        else if ((length == 16 || length == 13) & (firstnum == 4))
        {
            printf("VISA\n");           
        }
        else if ((length == 16) & (firstnum == 5 || firstnum == 2) & (secondnum < 6))
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID2\n");
        }
    }
    else
    {
        printf("INVALID1\n");  
    }
    return 0;
}

//below, validating the credit card is just checking if the last number of the sum is 0
bool validation(int sum)  
{
    int lastnum = sum % 10; // this gets the last number
    if (lastnum == 0)
    {
        return true; 
    }
    else
    {
        return false;         
    }
    
}
