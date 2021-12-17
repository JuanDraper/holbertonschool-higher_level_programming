#include "hash_tables.h"
/*
* hash_djbd - function that hashes
* @str: the string that will be hashed
* Return: the hashed string
*/
unsigned long int hash_djb2(const unsigned char *str)
{
    unsigned long int hash;
    int c;

    hash = 5381;
    while ((c = *str++))
    {
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
    }
    return (hash);
}
