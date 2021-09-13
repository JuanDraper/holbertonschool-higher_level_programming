#include "lists.h"
/**
* is_palindrome - blabla
* @head: blablalb
* Return: blablalb
*/
int is_palindrome(listint_t **head)
{
	int d[10000];
	short c, i;

	if (!head || !*head)
		return (1);
	for (c = 0; *head; *head = (*head)->next)
		d[c++] = (*head)->n;
	for (i = 0; i < c; i++, c--)
		if (d[i] != d[c - 1])
			return (0);
	return (1);
}
