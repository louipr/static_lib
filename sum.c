#include "sum.h"
#include "add.h"

int sum(int ilist[],int ilist_size)
{
    int isum = 0; 
    for(int i = 0; i < ilist_size; i++)
    {
        isum = add(ilist[i],isum);
    }

    return isum;
}