#include "lists.h"
#include <stdlib.h>
/**
* insert_node - blabla.
* @head: blabla
* @number: blbla.
* Return: blabla.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *iterator = *head;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!*head)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	if (number <= (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (iterator->next)
		{
			if (number <= iterator->next->n)
			{
				new->next = iterator->next;
				iterator->next = new;
				return (new);
			}
			iterator = iterator->next;
		}
	}
	new->next = NULL;
	iterator->next = new;
	return (new);
}
