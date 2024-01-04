#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	int i = 0, j;
	listint_t *temp, *curr;

	if (list == NULL)
	{
		return (0);
	}
	curr = list;
	temp = list;
	if (list->next == NULL)
	{
		return (0);
	}
	list = list->next;
	while (list != NULL)
	{
		j = 0;
		while (curr != NULL)
		{
			if (curr == list)
			{
				return (1);
			}
			if (j == i)
			{
				break;
			}
			j++;
			curr = curr->next;
		}
		curr = temp;
		list = list->next;
		i++;
	}
	return (0);
}
