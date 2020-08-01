// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#include "dictionary.h"

// Represents number of children for each node in a trie
#define N 27

// Represents a node in a trie
typedef struct node
{
    bool is_word;
    struct node *children[N];
}
node;

// Represents a trie
node *root;

int count;

bool unloadHelper(node *toUnload);

// Hashes letter to a number between 0 and 26, inclusive,
unsigned int hash(char letter)
{
    if (tolower(letter) == 39)
    {
        return 26;
    }
    return tolower(letter) - 'a';
}



// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize trie
    root = malloc(sizeof(node));
    if (root == NULL)
    {
        return false;
    }
    root->is_word = false;
    for (int i = 0; i < N; i++)
    {
        root->children[i] = NULL;
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

    // Insert words into trie
    while (fscanf(file, "%s", word) != EOF)
    {
        int j = strlen(word);
        node *temp = root;
        for (int i = 0; i < j; i++) //for every letter in word, create path in trie
        {
            int index = hash(word[i]); //create a hash for each letter
            if (temp->children[index] == NULL) //if path in letters is empty, make new path
            {
                node *newPath = malloc(sizeof(node));
                if (newPath == NULL) //if no new memory can be allocated
                {
                    unload();
                    return false;
                }
                temp->children[index] = newPath;
                temp = newPath;
                for (int k = 0; k < N; k++)
                {
                    temp->children[k] = NULL;
                }
                temp->is_word = false;
            }
            else //if path is open, move to next deeper path
            {
                temp = temp->children[index];
            }
        }
        temp->is_word = true; //at end of word from dictionary, set to true to show its end of a valid word
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
    int j = strlen(word);
    bool flag = false;
    node *trav = root;
    for (int i = 0; i < j; i++)
    {
        int index = hash(word[i]);
        if (trav->children[index] == NULL)
        {
            if (trav->is_word && i == j)
            {
                return true;
            }
            return false;
        }
        else //if path is open, move to next deeper path
        {
            trav = trav->children[index];
            if (trav->is_word)
            {
                flag = true;
            }
            else
            {
                flag = false;
            }
        }
    }
    return flag;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    /*
    free(root); //temp for now;
    return true;
    */

    node *toUnload = root;
    bool unLoaded = unloadHelper(toUnload);
    return unLoaded;
}

bool unloadHelper(node *toUnload)
{
    if (toUnload != NULL)
    {
        for (int i = 0; i < N; i++)
        {
            if (toUnload->children[i] != NULL)
            {
                unloadHelper(toUnload->children[i]);
            }
        }
        free(toUnload);
        return true;
    }
    return false;

}
