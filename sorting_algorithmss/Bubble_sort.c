#include<stdio.h>
#include<conio.h>
void main()
{
    int a[]={1,4,6,9,0};
    int i,j,temp,n=sizeof(a)/sizeof(a[0]);
    for(i=0;i<n-1;i++)
    {
        for(j=0;j<n-i-1;j++)
        {
            if(a[j]>a[j+1])
            {
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
    }
    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
}
