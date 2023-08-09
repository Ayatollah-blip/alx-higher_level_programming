#include "lists,h"

listint_t *insert_node(listint_t **head, int number)
{
listint_t temp = head;
listint_t current = head;
listint_t new = malloc(sizeof(head));

new -> n = number;
new -> next = NULL;

while(temp -> next != NULL)
{
	if(temp -> n > number)
	{
 		current = temp;
		temp = new;
		new -> next = current;
		return (temp);
	}
	temp = temp -> next;
}
return (NULL);
}
