<<<<<<< HEAD
/**
 * check_cycle - checks a linked list to determine if there is a cycle
 * @list: pointer to the head of the list
 * Return: 1 if has cycle, 0 if no cycle
 */

#include "lists.h"
#include <stdio.h>

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
	{
		return (0);
	}

	fast = list->next;
	slow = list;

	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		if (fast == slow)
		{
			return (1);
		}
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
=======
#include "lists.h"
/**
 * check_cycle - checks whether a list cycles or not
 * @list: singly linked list
 * Return: 0 No Cycling 1 Cycling
 */
int check_cycle(listint_t *list)
{
listint_t *curr = NULL, *tmp = NULL;
if (list == NULL)
return (0);
curr = list;
tmp = list->next;
while (tmp != NULL && tmp->next != NULL)
{
if (tmp == curr)
return (1);
curr = curr->next;
tmp = (tmp->next)->next;
}
return (0);
>>>>>>> d1c8dd8cb4c8884088973472636c6157590e83d8
}
