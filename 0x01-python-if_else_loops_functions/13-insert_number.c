#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
listint_t *temp = *head;
listint_t new = malloc(sizeof(listint_t));

if(new == NULL)
	return (NULL);

new -> n = number;

	if(temp == NULL || temp -> n >= number)
	{
 		new -> next = temp;
		*head = new;
		return (new);
	}
	while(temp && temp -> next && temp -> next -> n < number)
		temp = temp -> next;
	new -> next = temp -> next;
	temp -> next = new

}
return (new);
}
