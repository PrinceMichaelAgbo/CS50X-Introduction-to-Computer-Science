// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 26

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Represents a hash table
node *hashtable[N];

//counts the number of words loaded
unsigned int count = 0;

void unloadHelper(node *toUnload);




// Hashes word to a number between 0 and 25, inclusive, based on its first letter
unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < N; i++)
    {
        hashtable[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)
    {
        int index = hash(word);
        node *temp = malloc(sizeof(node));
        if (temp == NULL)
        {
            unload();
            return false;
        }
        strcpy(temp->word, word);
        if (hashtable[index] == NULL)
        {
            temp->next = NULL;
        }
        else
        {
            temp->next = hashtable[index];
        }
        hashtable[index] = temp;
        count++;
    }
    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return count;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int index = hash(word);
    int j = strlen(word);
    node *trav;
    trav = hashtable[index];
    char *newWord = malloc(j + 1);
    //strcpy(newWord, word);
    newWord[j] = '\0';
    for (int i = 0; i < j; i++)
    {
        newWord[i] = tolower(word[i]);
    }
    int num = 0;
    while (trav != NULL)
    {
        if (strcmp(trav->word, newWord) == 0 ) //find way to use strcasecmp
        {
            free(newWord);
            return true;
        }
        trav = trav->next;
    }
    free(newWord);
    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    //free(*hashtable);
    //return true;
    node *toUnload;
    for (int i = 0; i < N; i++)
    {
        if (hashtable[i] != NULL)
        {
            toUnload = hashtable[i];
            unloadHelper(toUnload);
        }
        if (i == (N - 1))
        {
            return true;
        }
    }
    return false;
}

void unloadHelper(node *toUnload)
{
    if (toUnload->next == NULL)
    {
        free(toUnload);
    }
    else
    {
        unloadHelper(toUnload->next);
        free(toUnload);
    }
}

