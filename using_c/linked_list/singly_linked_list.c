#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

// A linked list node
struct node
{
  int data;
  struct node *next;
};

void push(struct node** head_ref, int new_data){
    struct node* new_node = (struct node*)malloc(sizeof(struct node));
    new_node->data = new_data;
    new_node->next = *head_ref;
    *head_ref = new_node;
}

void insertAfter(struct node* prev, int new_data){

    if(prev == NULL){
        printf("Previous node cannot be NULL!!\n");
    }

    struct node* new_node = (struct node*)malloc(sizeof(struct node));
    new_node->data = new_data;
    new_node->next = prev->next;
    prev->next = new_node;
}

/* Given a reference (pointer to pointer) to the head
   of a list and an int, appends a new node at the end  */
void append(struct node** head_ref, int new_data)
{

    struct node* new_node = (struct node*)malloc(sizeof(struct node));
    struct node *last = *head_ref;

    new_node->data  = new_data;
    new_node->next = NULL;

    if (*head_ref == NULL)
    {
       *head_ref = new_node;
       return;
    }

    while (last->next != NULL)
        last = last->next;

    last->next = new_node;
    return;
}
// This function prints contents of linked list starting from head
void printList(struct node *node)
{
  while (node != NULL)
  {
     printf(" %d ", node->data);
     node = node->next;
  }
  printf("\n");
}
int main(){

     struct node* head = NULL;

     append(&head, 1);
     append(&head, 2);
     append(&head, 3);
     printList(head);

     push(&head, 100);
     push(&head, 200);
     printList(head);

     insertAfter(head->next, 199);
     printList(head);
     insertAfter(head, 187);
     printList(head);
}
