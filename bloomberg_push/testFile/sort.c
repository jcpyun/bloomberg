#include <math.h>
#include <err.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>


int main()
{
    int nmax = 50
    FILE *orig, *prod;
    orig = fopen("listOfSymbols.txt","r");
    prod = fopen("newlist.txt","w");
    if (!orig) err(errno, "open read failed");
    if (!prod) err(errno, "write read failed");
    
    for (int n=0; n<nmax; n++)
    {
        int scan = fscanf(orig,"%f\n",&
