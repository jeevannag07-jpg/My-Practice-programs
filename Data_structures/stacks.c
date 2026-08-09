#include <stdio.h>

#define MAX 10

int stack[MAX], TOP = -1;

void push();
void pop();
void display();

int main()
{
    int choice;

    do
    {
        printf("\n1. Push");
        printf("\n2. Pop");
        printf("\n3. Display");
        printf("\n4. Exit");

        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                push();
                break;

            case 2:
                pop();
                break;

            case 3:
                display();
                break;

            case 4:
                printf("\nExit point");
                break;

            default:
                printf("\nPlease enter a valid choice (1/2/3/4)");
        }

    } while(choice != 4);

    return 0;
}


void push()
{
    int x;

    if(TOP == MAX - 1)
    {
        printf("\nStack is full");
    }
    else
    {
        printf("\nEnter a value to be pushed: ");
        scanf("%d", &x);

        TOP = TOP + 1;
        stack[TOP] = x;
    }
}


void pop()
{
    if(TOP == -1)
    {
        printf("\nStack is empty");
    }
    else
    {
        printf("\nThe popped element is %d", stack[TOP]);
        TOP = TOP - 1;
    }
}


void display()
{
    int i;

    if(TOP == -1)
    {
        printf("\nStack is empty");
    }
    else
    {
        printf("\nThe elements in the stack are:\n");

        for(i = TOP; i >= 0; i--)
        {
            printf("%d\n", stack[i]);
        }
    }
}