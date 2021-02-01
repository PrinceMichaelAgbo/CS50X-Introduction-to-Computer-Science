#define _XOPEN_SOURCE
#include <unistd.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

bool validate_hash(int length, string argv[], string hash);
void crack(int argc, string argv[]);

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        crack(argc, argv);
    }
    else
    {
        printf("Usage: ./crack hash\n"); 
        return 1;        
    }
}

void crack(int argc, string argv[]) 
{  
    int length = strlen(argv[1]), stop = 0, counter = 0;
    int place1 = 0;
    char salt[2];
    salt[0] = argv[1][0];
    salt[1] = argv[1][1];
    char letter1, letter2, letter3, letter4, letter5;
    int letternum1 = 0, letternum2 = 0, letternum3 = 0, letternum4 = 0, letternum5 = 0;
    int places = 1, aplaces;
    while (stop == 0)
    { 
        aplaces = places + 1;
        char passw[aplaces];
        if (places == 1)
        {
            if (letternum1 < 26)
            {
                letter1 = letternum1 + 65;                
            }              
            else
            {
                letter1 = letternum1 + 71;                
            }
            passw[0] = letter1;
            letternum1 += 1;
            if (letternum1 > 51)
            {
                places += 1;
                letternum1 = 0;
            }               
        }

        else if (places == 2)
        {
            if (letternum1 < 26)
            {
                letter1 = letternum1 + 65;
            }              
            else
            {
                letter1 = letternum1 + 71;
            }              
            passw[0] = letter1;
            if (letternum2 < 26)
            {
                letter2 = letternum2 + 65;
            }                
            else
            {
                letter2 = letternum2 + 71;
            }
            passw[1] = letter2;
            letternum2 += 1;
            if (letternum2 > 51)
            {
                letternum1 += 1;
                letternum2 = 0;                
            }                        
            if (letternum1 > 51)
            {
                places += 1;
                letternum1 = 0;
            }                          
        }
          
        else if (places == 3)
        {
            if (letternum1 < 26)
            {
                letter1 = letternum1 + 65;
            }              
            else
            {
                letter1 = letternum1 + 71;
            }              
            passw[0] = letter1;
            if (letternum2 < 26)
            {
                letter2 = letternum2 + 65;
            }              
            else
            {
                letter2 = letternum2 + 71;
            }              
            passw[1] = letter2;
            if (letternum3 < 26)
            {
                letter3 = letternum3 + 65;
            }                 
            else
            {
                letter3 = letternum3 + 71;
            }              
            passw[2] = letter3;
            letternum3 += 1;
            if (letternum3 > 51)
            {
                letternum2 += 1;
                letternum3 = 0; 
            }              
            if (letternum2 > 51)
            {
                letternum1 += 1;
                letternum2 = 0;
            }               
            if (letternum1 > 51)
            {
                places += 1;
                letternum1 = 0;
            }              
        }
        
        else if (places == 4)
        {
            if (letternum1 < 26)
            {
                letter1 = letternum1 + 65;
            }              
            else
            {
                letter1 = letternum1 + 71;
            }              
            passw[0] = letter1;
            if (letternum2 < 26)
            {
                letter2 = letternum2 + 65;
            }              
            else
            {
                letter2 = letternum2 + 71;
            }              
            passw[1] = letter2;
            if (letternum3 < 26)
            {
                letter3 = letternum3 + 65;
            }
            else
            {
                letter3 = letternum3 + 71;
            }
            passw[2] = letter3;
            if (letternum4 < 26)
            {
                letter4 = letternum4 + 65;
            }
            else
            {
                letter4 = letternum4 + 71;
            }
            passw[3] = letter4;
            letternum4 += 1;
            if (letternum4 > 51)
            {
                letternum3 += 1;
                letternum4 = 0;
            } 
            if (letternum3 > 51)
            {
                letternum2 += 1;
                letternum3 = 0;
            }
            if (letternum2 > 51)
            {
                letternum1 += 1;
                letternum2 = 0;
            }
            if (letternum1 > 51)
            {
                places += 1;
                letternum1 = 0;
            }
        }
          
        else if (places == 5)
        {
            if (letternum1 < 26)
            {
                letter1 = letternum1 + 65;
            }
            else
            {
                letter1 = letternum1 + 71;
            }
            passw[0] = letter1;
            if (letternum2 < 26)
            {
                letter2 = letternum2 + 65;
            }
            else
            {
                letter2 = letternum2 + 71;
            }
            passw[1] = letter2;
            if (letternum3 < 26)
            {
                letter3 = letternum3 + 65;
            }
            else
            {
                letter3 = letternum3 + 71;
            }
            passw[2] = letter3;
            if (letternum4 < 26)
            {
                letter4 = letternum4 + 65;
            }
            else
            {
                letter4 = letternum4 + 71;
            }
            passw[3] = letter4;
            if (letternum5 < 26)
            {
                letter5 = letternum5 + 65;
            }
            else
            {
                letter5 = letternum5 + 71;
            }
            passw[4] = letter5;
            letternum5 += 1;
            if (letternum5 > 51)
            {
                letternum4 += 1;
                letternum5 = 0;
            }
            if (letternum4 > 51)
            {
                letternum3 += 1;
                letternum4 = 0; 
            }
            if (letternum3 > 51)
            {
                letternum2 += 1;
                letternum3 = 0;
            }
            if (letternum2 > 51)
            {
                letternum1 += 1;
                letternum2 = 0;
            }
            if (letternum1 > 51)
            {
                places += 1;
                letternum1 = 0;
            }
        }

        string hash = crypt(passw, salt);
        bool valid_hash = validate_hash(length, argv, hash);
        if (valid_hash)
        {
            stop += 1;
            printf("%s\n", passw);
        }
    }           
}

bool validate_hash(int length, string argv[], string hash)
{
    int counter = 0;
    for (int i = 0; i < length; i++)
    {
        if (argv[1][i] == hash[i])
        {
            counter++;
        }
    }
    if (counter == length)
    {
        return true;
    }
    else
    {
        return false;
    }
}

