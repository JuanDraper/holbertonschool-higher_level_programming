#include "hash_tables.h"
/**
 * hash_table_create - it will create a new hash table
 * @size: the size the hash table will have
 * Return: the newly created hash table or NULL
 */
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *new;
	hash_node_t **nodes;

	if(size == 0)
	{
		return(NULL);
	}
	new = malloc(sizeof(hash_table_t));
	if(!new)
	{
		return(NULL);
	}
	new->size = size;
	nodes = calloc(size, sizeof(hash_node_t *));
	if(!nodes)
	{
		free(new);
		return(NULL);
	}
	new->array = nodes;
	return(new);
}

