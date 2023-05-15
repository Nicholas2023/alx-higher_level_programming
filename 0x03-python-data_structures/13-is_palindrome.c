#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a linked list
 * @head: Double pointer to the head of the list
 *
 * Return: Reversed linked list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 * compare_lists - Compares two linked lists
 * @list1: First linked list
 * @list2: Second linked list
 *
 * Return: 1 if lists are identical, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 && list2)
	{
		if (list1->n != list2->n)
			return (0);

		list1 = list1->next;
		list2 = list2->next;
	}

	return (1);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *second_half = NULL;
	int is_palindrome = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			slow = slow->next;
		}

		second_half = slow;
		prev_slow->next = NULL;

		reverse_list(&second_half);

		is_palindrome = compare_lists(*head, second_half);

		reverse_list(&second_half);

		if (prev_slow != NULL)
		{
			prev_slow->next = second_half;
		}
		else
		{
			*head = second_half;
		}
	}

	return (is_palindrome);
}
