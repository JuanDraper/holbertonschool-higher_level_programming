#include "lists.h"
#include <stdlib.h>

/**
*check_cycle - blablab
*@list: blabla
*Return: blablabl
**/

int check_cycle(listint_t *list)
{
if (!list)
return (0);
while (1)
{
if (list->next >= list || !list->next)
break;
list = list->next;
}
if (list->next)
return (1);
return (0);
}
