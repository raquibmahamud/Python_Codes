#include<stdio.h>
int main()
{
    int array[100];
    int i = 0;
    int p;


    while(scanf("%d",&array[i]))
    {
        if(0 == array[i])

        {
            break;
        }

        if(i>100)
        {
            printf("Overflow");
            break;
        }
        else
        {
         i++;


        }




    }

for(p=0;p<i;p++){
    printf("%d ",array[p]);
}

    return 0;
}
