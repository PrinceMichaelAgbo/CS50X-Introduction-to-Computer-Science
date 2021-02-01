#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool validate(int argc, string argv[]);
void encrypt(int number);

int main(int argc, string argv[]) //main function to direct flow and call other functions
{
    bool valid = validate(argc, argv);
    if (valid)
    {
        int number = atoi(argv[1]);
        encrypt(number);
    }
    else
    {
        printf("Usage: ./caesar key\n"); 
        return 1;
            
    }    
}
bool validate(int argc, string argv[]) //this function checks to make sure
// the program gets the right type and number of inputs 
{
    if (argc == 2) //only one user input in addition to the file execution is valid
    {
        int length = strlen(argv[1]), counter = 0;
        for (int i = 0; i < length; i++)
        {
            if (isdigit(argv[1][i])) //this counts the number of characters in the user input             //that are numbers
            {
                counter += 1;
            }
        }
        if (counter == length)//if all characters in the input are numbers, it is valid, else,         //it is invalid
        {
            return true;
        }
        else
        {
            return false;
        }        
    }
    else
    {
        return false;
    }    
}


void encrypt(int number)  // the function encrypts the plaintext by moving it
// the number of times requested by the user and outputs the ciphertext
{  
    string plain = get_string("plaintext: "); //user input
    printf("ciphertext: ");
    int length = strlen(plain);
    char array[length];
    for (int i = 0; i < length; i++)
    {
        if isalpha(plain[i]) //if its a letter, encrypt it, else, leave it as is
        {
            int letternum = plain[i];
            letternum = letternum + (number % 26); 
            if isupper(plain[i])
            {
                if (letternum > 90)
                {
                    letternum = ((letternum % 90) + 65) - 1;
                }
            }
            else
            {
                if (letternum > 122)
                {
                    letternum = ((letternum % 122) + 97) - 1;
                }
            }
            char letter = letternum;
            array[i] = letter;
        }
        else
        {
            array[i] = plain[i];
        }           
        printf("%c", array[i]);
    }
    printf("\n");
}

