#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool validate(int argc, string argv[]);
void encrypt(string argv[1], int length);

int main(int argc, string argv[]) //main function to direct flow and call other functions
{
    
    bool valid = validate(argc, argv);
    if (valid)
    {
        int length = strlen(argv[1]);
        encrypt(argv, length);
    }
    else
    {
        printf("Usage: ./vigenere keyword\n"); 
        return 1;
            
    }    
}
bool validate(int argc, string argv[]) //this function checks to make sure
// the program gets the right type and number of inputs 
{
    if (argc == 2) //only one user input in addition to the file execution is valid
    {
        int length = strlen(argv[1]);
        int counter = 0;
        for (int i = 0; i < length; i++)
        {
            if (isalpha(argv[1][i])) //this counts the number of characters in the user input             //that are letters
            {
                counter += 1;
            }
        }
        if (counter == length)//if all characters in the input are letters, it is valid, else,         //it is invalid
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


void encrypt(string argv[1], int length)  // the function encrypts the plaintext by moving it
// the number of times requested by the user and outputs the ciphertext
{  
    string plain = get_string("plaintext: "); //user input
    printf("ciphertext: ");
    int plainlength = strlen(plain), index, keyletternum, counter = 0;
    char array[plainlength];
    for (int i = 0; i < plainlength; i++)
    {
        if isalpha(plain[i]) //if its a letter, encrypt it, else, leave it as is
        {
            int letternum = plain[i];
            index = counter % length;
            counter++;
            keyletternum = argv[1][index];
            //printf("%i\n", index);
            if (keyletternum >= 65 & keyletternum <= 90)
            {
                letternum = letternum + (keyletternum - 65); 
            }
            else if (keyletternum >= 97 & keyletternum <= 122)
            {
                letternum = letternum + (keyletternum - 97);  
            }            
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
