#include<stdio.h>
void main()
{
    int a[]={7,3,6,1,9,8};
    int i,curr,prev,n=sizeof(a)/sizeof(a[0]);
    for(i=1;i<n;i++)
    {
        curr=a[i];
        prev=i-1;
        while(prev>=0 && a[prev]>curr)
        {
            a[prev+1]=a[prev];
            prev--;
        }
        a[prev+1]=curr;
    }
    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
}